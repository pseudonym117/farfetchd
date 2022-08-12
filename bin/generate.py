from __future__ import annotations

import asyncio
import collections
import dataclasses
import enum
import os
import re
import sys

from html.parser import HTMLParser

from typing import Dict, List

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

    print("writing models...")
    await write_models(f"{output_dir}/models", parser.section_types)

    print("done")


async def write_models(output_dir: str, section_types: Dict[str, List[TypeInfo]]):
    type_to_section_name = {}
    for section, types in section_types.items():
        for type in types:
            type_to_section_name[type.name] = section

    env = jinja2.Environment(
        loader=jinja2.PackageLoader("generate"),
        autoescape=jinja2.select_autoescape(),
        enable_async=True,
    )
    model_template = env.get_template("model_template.py.tmpl")

    os.makedirs(output_dir, exist_ok=True)
    for section, types in section_types.items():
        required_types = set()
        for type in types:
            for imp in type.extra_type_imports():
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
        if any([type.uses_lists() for type in types]):
            typing_imports.append("List")
        if any([type.is_generic() for type in types]):
            typing_imports.extend(["Generic", "TypeVar"])
        if typing_imports:
            extra_imports.insert(0, ExtraImport("typing", sorted(typing_imports)))

        rendered = await model_template.render_async(
            types=types, extra_imports=extra_imports
        )

        blacked = black.format_str(rendered, mode=black.FileMode())

        with open(f"{output_dir}/{section}.py", "w+") as f:
            f.write(blacked)

    if not os.path.exists(f"{output_dir}/__init__.py"):
        with open(f"{output_dir}/__init__.py", "w+") as f:
            pass


class State(enum.Enum):
    NONE = 0
    SECTION = 1
    API_NAME = 2
    TYPE_NAME = 3
    TYPE_INFO_START = 4
    TYPE_INFO_PROP_NAME = 5
    TYPE_INFO_DESCRIPTION = 6
    TYPE_INFO_TYPE = 7


type_remapping = {
    "string": "str",
    "integer": "int",
    "boolean": "bool",
}

type_builtins = {"str", "int", "bool"}

complex_type_re = re.compile("(list )?(\w+ )?\\(?(\w+)\\)?")


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


@dataclasses.dataclass
class TypeInfo:
    name: str
    properties: List[PropertyInfo]

    def is_generic(self):
        return self.name == "NamedAPIResource" or self.name == "APIResource"

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


class ApiDefBuilder(HTMLParser):
    section_blocklist = [
        "contents",
        "information",
        "fair use policy",
        "slack",
        "wrapper libraries",
        # todo: need to parse this section in order to support pagination
        "resource lists/pagination",
    ]

    def __init__(self) -> None:
        super().__init__()
        # section -> endpoint -> def
        self.api_spec: Dict[str, Dict[str, any]] = {}

        # section -> typename -> def
        self.section_types: Dict[str, List[TypeInfo]] = {}

        self._state = State.NONE

        self._current_section: str | None = None

        self._current_type: TypeInfo | None = None
        self._current_property: PropertyInfo | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "h2":
            self._state = State.SECTION
        elif tag == "h3":
            self._state = State.API_NAME
        elif tag == "h4":
            self._state = State.TYPE_NAME
        elif tag == "tbody" and self._state == State.TYPE_INFO_START:
            self._state = State.TYPE_INFO_PROP_NAME

    def handle_endtag(self, tag: str) -> None:
        if self._state == State.TYPE_INFO_START and tag == "tbody":
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

    def handle_data(self, data: str) -> None:
        data = self.sanitize(data)
        if self._state == State.SECTION:
            data = data.lower()
            if data not in self.section_blocklist:
                self._current_section = data
                if data not in self.api_spec:
                    self.api_spec[data] = {}
                if data not in self.section_types:
                    self.section_types[data] = []
            self._state = State.NONE
        elif self._state == State.API_NAME:
            if self._current_section:
                self.api_spec[self._current_section][data] = {}
            self._state = State.NONE
        elif self._state == State.TYPE_NAME:
            if self._current_section:
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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect usage")
        print("expected: generate.py <output_directory>")
        exit(-1)
    asyncio.run(main(sys.argv[1]))
