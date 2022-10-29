from __future__ import annotations

import asyncio
import collections
import dataclasses
import enum
import json
import os
import re
import sys

from html.parser import HTMLParser

from typing import Any, Dict, List

import aiohttp
import black
import jinja2


async def main(output_dir: str):
    if not os.path.exists(output_dir):
        print(f'directory "{output_dir}" does not exist!')
        exit(-1)
    if not os.path.isdir(output_dir):
        print(f'could not write to directory "{output_dir}": is not a directory')
        exit(-1)

    print("reading data from pokeapi...")
    async with aiohttp.ClientSession() as session:
        async with session.get("https://pokeapi.co/docs/v2") as resp:
            if resp.status != 200:
                print("error fetching API docs")
                exit(-1)
            raw = await resp.text()

    print("parsing response...")
    parser = ApiDefBuilder()
    parser.feed(raw)

    env = jinja2.Environment(
        loader=jinja2.PackageLoader("generate"),
        autoescape=jinja2.select_autoescape(),
        enable_async=True,
    )

    print("writing models...")
    await write_models(env, f"{output_dir}/models", parser.section_types)

    print("writing definitions...")
    await write_defs(env, f"{output_dir}/defs", parser.api_spec, parser.section_types)

    print("done")


async def write_models(
    env: jinja2.Environment, output_dir: str, section_types: Dict[str, List[TypeInfo]]
):
    # move generic models into separate file
    assert "generic" not in section_types

    generic_section_types = []
    for defined_types in section_types.values():
        to_move = []
        for defined_type in defined_types:
            if defined_type.is_generic():
                to_move.append(defined_type)
        for defined_type in to_move:
            defined_types.remove(defined_type)
        generic_section_types.extend(to_move)
    section_types["generic"] = generic_section_types

    type_to_section_name = {}
    for section, defined_types in section_types.items():
        for defined_type in defined_types:
            type_to_section_name[defined_type.name] = section
    model_template = env.get_template("model_template.py.jinja2")

    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/__init__.py", "w+", encoding="utf-8"):
        for section, defined_types in section_types.items():
            if not defined_types:
                continue

            required_types = set()
            for defined_type in defined_types:
                for imp in defined_type.extra_type_imports():
                    required_types.add(imp)

            extra_import_dict = collections.defaultdict(lambda: [])

            if required_types:
                for required in required_types:
                    from_module = type_to_section_name[required]
                    extra_import_dict[from_module].append(required)

            if section in extra_import_dict:
                del extra_import_dict[section]

            extra_imports = sorted(
                [
                    ExtraImport(f".{module}", sorted(classes))
                    for module, classes in extra_import_dict.items()
                ],
                key=lambda imp: imp.module,
            )

            typing_imports = []
            if any([type.uses_lists() for type in defined_types]):
                typing_imports.append("List")
            if typing_imports:
                extra_imports.insert(0, ExtraImport("typing", sorted(typing_imports)))

            rendered = await model_template.render_async(
                types=defined_types, extra_imports=extra_imports
            )

            blacked = black.format_str(rendered, mode=black.FileMode())

            with open(f"{output_dir}/{section}.py", "w+", encoding="utf-8") as file:
                file.write(blacked)


async def write_defs(
    env: jinja2.Environment,
    output_dir: str,
    api_spec: Dict[str, List[ApiInfo]],
    section_types: Dict[str, List[TypeInfo]],
):
    type_to_section_name = {}
    for section, defined_types in section_types.items():
        for defined_type in defined_types:
            type_to_section_name[defined_type.name] = section

    real_apis = {
        section: [api for api in apis if api.url]
        for section, apis in api_spec.items()
        if apis
    }

    api_template = env.get_template("api_template.py.jinja2")

    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/__init__.py", "w+", encoding="utf-8") as init_py:
        init_lines = []
        for section, apis in real_apis.items():
            required_types = set([api.response_typename for api in apis])
            extra_import_dict = collections.defaultdict(lambda: [])

            if required_types:
                for required in required_types:
                    from_module = type_to_section_name[required]
                    extra_import_dict[from_module].append(required)

            extra_imports = sorted(
                [
                    ExtraImport(f"..models.{module}", sorted(classes))
                    for module, classes in extra_import_dict.items()
                ],
                key=lambda imp: imp.module,
            )

            rendered = await api_template.render_async(
                section=section, endpoints=apis, extra_imports=extra_imports
            )

            blacked = black.format_str(rendered, mode=black.FileMode())
            # blacked = rendered

            with open(f"{output_dir}/{section}.py", "w+", encoding="utf-8") as file:
                file.write(blacked)

            init_lines.append(
                f"from .{section} import {','.join(sorted([api.name for api in apis]))}"
            )

        raw_init = "\n".join(init_lines)
        blacked = black.format_str(raw_init, mode=black.FileMode())
        init_py.write(blacked)

    # print(json.dumps(real_apis, indent=2, cls=DataclassJsonEncoder))


class DataclassJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> str:
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


class State(enum.Enum):
    NONE = 0
    SECTION = 1
    API_NAME = 10
    API_NAME_DONE = 11
    API_DESC = 12
    API_DESC_DONE = 13
    API_URL = 14
    TYPE_NAME = 20
    TYPE_INFO_START = 21
    TYPE_INFO_PROP_NAME = 22
    TYPE_INFO_DESCRIPTION = 23
    TYPE_INFO_TYPE = 24


type_remapping = {
    "string": "str",
    "integer": "int",
    "boolean": "bool",
}

type_builtins = {"str", "int", "bool"}

complex_type_re = re.compile(r"(list )?(\w+ )?\(?(\w+)\)?")


@dataclasses.dataclass
class ExtraImport:
    module: str
    classes: List[str]


@dataclasses.dataclass
class PropertyInfo:
    name: str
    description: str
    type: PropertyType | str


@dataclasses.dataclass
class PropertyType:
    @staticmethod
    def from_raw(raw_str: str) -> PropertyType:
        if raw_str in type_remapping:
            remapped = type_remapping[raw_str]
            return PropertyType(remapped, None, False)
        match = complex_type_re.match(raw_str)
        if match:
            list_type, ref_type, actual_type = match.groups()
            if ref_type:
                ref_type = ref_type.strip()
            if actual_type in type_remapping:
                actual_type = type_remapping[actual_type]
            return PropertyType(actual_type, ref_type, list_type is not None)
        return PropertyType(raw_str, None, False)

    property_type: str
    reference_type: str | None
    is_list: bool

    def __str__(self) -> str:
        if self.reference_type:
            ref = f"{self.reference_type}[{self.property_type}]"
        else:
            ref = self.property_type

        if self.is_list:
            return f"List[{ref}]"
        return ref


generic_types = {
    "NamedAPIResource",
    "APIResource",
    # todo: handle adding generic type to this type in APIs
    "NamedAPIResourceList",
}


@dataclasses.dataclass
class TypeInfo:
    name: str
    properties: List[PropertyInfo]

    def is_generic(self):
        return self.name in generic_types

    def uses_lists(self) -> bool:
        return any([prop.type.is_list for prop in self.properties])

    def extra_type_imports(self) -> List[str]:
        ref_types = [
            prop.type.reference_type
            for prop in self.properties
            if prop.type.reference_type
        ]
        final_types = [
            prop.type.property_type
            for prop in self.properties
            if prop.type.property_type not in type_builtins
        ]
        return [*ref_types, *final_types]


@dataclasses.dataclass
class ApiInfo:
    name: str
    description: str
    url: str
    response_typename: str

    def url_without_args(self):
        end_index = self.url.find("{")
        if end_index == -1:
            return self.url
        return self.url[:end_index]

    def args(self) -> List[(str, str)]:
        match = re.search(r"/\{(id)?( or )?(name)?\}/", self.url)
        if match:
            id_arg, _, name_arg = match.groups()
            return [i for i in [(id_arg, "int"), (name_arg, "str")] if i[0]]
        return []


class ApiDefBuilder(HTMLParser):
    section_blocklist = {
        "contents",
        "information",
        "fair use policy",
        "slack",
        "wrapper libraries",
    }

    section_without_api = {"pagination"}

    def __init__(self) -> None:
        super().__init__()
        # section -> endpoint -> def
        self.api_spec: Dict[str, List[ApiInfo]] = {}

        # section -> typename -> def
        self.section_types: Dict[str, List[TypeInfo]] = {}

        self._state = State.NONE

        self._current_section: str | None = None
        self._current_api: ApiInfo | None = None
        self._current_type: TypeInfo | None = None
        self._current_property: PropertyInfo | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        if tag == "h2":
            self._state = State.SECTION
        elif tag == "h3":
            if self._current_section not in self.section_without_api:
                self._state = State.API_NAME
        elif tag == "div" and self._state == State.API_NAME_DONE:
            self._state = State.API_DESC
        elif tag == "p" and self._state == State.API_DESC_DONE:
            self._state = State.API_URL
        elif tag == "h4":
            self._state = State.TYPE_NAME
        elif tag == "tbody" and self._state == State.TYPE_INFO_START:
            self._state = State.TYPE_INFO_PROP_NAME

    def handle_endtag(self, tag: str):
        if self._state == State.API_DESC and tag == "div":
            self._state = State.API_DESC_DONE
        elif self._state == State.API_URL and tag == "p":
            self._state = State.NONE
        elif self._state == State.TYPE_INFO_START and tag == "tbody":
            self._state = State.NONE
        elif self._state == State.TYPE_INFO_PROP_NAME and tag == "td":
            self._state = State.TYPE_INFO_DESCRIPTION
        elif self._state == State.TYPE_INFO_DESCRIPTION and tag == "td":
            self._state = State.TYPE_INFO_TYPE
        elif self._state == State.TYPE_INFO_TYPE and tag == "td":
            self._current_property.type = PropertyType.from_raw(
                self._current_property.type
            )
            self._current_type.properties.append(self._current_property)
            self._current_property = PropertyInfo("", "", "")
            self._state = State.TYPE_INFO_PROP_NAME

    def handle_data(self, data: str):
        data = self.sanitize(data)
        if self._state == State.SECTION:
            data = data.lower()
            if data not in self.section_blocklist:
                # split on / and take last index to support pagination
                section_name = data.split("/")[-1]
                self._current_section = section_name
                if section_name not in self.api_spec:
                    self.api_spec[section_name] = []
                if section_name not in self.section_types:
                    self.section_types[section_name] = []
            self._state = State.NONE
        elif self._state == State.API_NAME:
            data = self.correct_api_name(data)
            if self._current_section:
                self._current_api = ApiInfo(data, "", None, None)
                # todo: write this at the end instead of immediately
                self.api_spec[self._current_section].append(self._current_api)
            self._state = State.API_NAME_DONE
        elif self._state == State.API_DESC:
            if self._current_api:
                self._current_api.description += data
        elif self._state == State.API_URL:
            if self._current_api:
                self._current_api.url = data
        elif self._state == State.TYPE_NAME:
            if self._current_section:
                # write as API return type if not set
                if self._current_api and not self._current_api.response_typename:
                    self._current_api.response_typename = data

                new_type = TypeInfo(data, [])
                self.section_types[self._current_section].append(new_type)
                self._current_type = new_type
                self._current_property = PropertyInfo("", "", "")
                self._state = State.TYPE_INFO_START
            else:
                self._state = State.NONE
        elif self._state == State.TYPE_INFO_PROP_NAME:
            if self._current_property:
                self._current_property.name += data
            else:
                self._state = State.NONE
        elif self._state == State.TYPE_INFO_DESCRIPTION:
            if self._current_property:
                self._current_property.description += data
            else:
                self._state = State.TYPE_INFO_TYPE
        elif self._state == State.TYPE_INFO_TYPE:
            if self._current_property:
                self._current_property.type += data
            else:
                self._state = State.NONE

    def sanitize(self, data: str) -> str:
        return data.replace("é", "e")

    def correct_api_name(self, data: str) -> str:
        return "_".join(data.lower().split())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect usage")
        print("expected: generate.py <output_directory>")
        exit(-1)
    asyncio.run(main(sys.argv[1]))
