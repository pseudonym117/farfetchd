"""
!!Generated code!!

Do not modify directly.

Generation script is located @ //farfetchd/bin/generate.py
"""

from __future__ import annotations
from dataclasses import dataclass


from typing import (
    Generic,
    List,
    TypeVar,
)

from .encounters import (
    EncounterConditionValue,
    EncounterMethod,
)

from .games import (
    Generation,
    Version,
    VersionGroup,
)


T = TypeVar("T")


@dataclass
class Language:
    # The identifier for this resource.
    id: int
    # The name for this resource.
    name: str
    # Whether or not the games are published in this language.
    official: bool
    # The two-letter code of the country where this language is spoken. Note that it is not unique.
    iso639: str
    # The two-letter code of the language. Note that it is not unique.
    iso3166: str
    # The name of this resource listed in different languages.
    names: List[Name]


@dataclass
class APIResource(Generic[T]):
    # The URL of the referenced resource.
    url: str


@dataclass
class Description:
    # The localized description for an API resource in a specific language.
    description: str
    # The language this name is in.
    language: NamedAPIResource[Language]


@dataclass
class Effect:
    # The localized effect text for an API resource in a specific language.
    effect: str
    # The language this effect is in.
    language: NamedAPIResource[Language]


@dataclass
class Encounter:
    # The lowest level the Pokemon could be encountered at.
    min_level: int
    # The highest level the Pokemon could be encountered at.
    max_level: int
    # A list of condition values that must be in effect for this encounter to occur.
    condition_values: List[NamedAPIResource[EncounterConditionValue]]
    # Percent chance that this encounter will occur.
    chance: int
    # The method by which this encounter happens.
    method: NamedAPIResource[EncounterMethod]


@dataclass
class FlavorText:
    # The localized flavor text for an API resource in a specific language. Note that this text is left unprocessed as it is found in game files. This means that it contains special characters that one might want to replace with their visible decodable version. Please check out this issue to find out more.
    flavor_text: str
    # The language this name is in.
    language: NamedAPIResource[Language]
    # The game version this flavor text is extracted from.
    version: NamedAPIResource[Version]


@dataclass
class GenerationGameIndex:
    # The internal id of an API resource within game data.
    game_index: int
    # The generation relevent to this game index.
    generation: NamedAPIResource[Generation]


@dataclass
class MachineVersionDetail:
    # The machine that teaches a move from an item.
    machine: APIResource
    # The version group of this specific machine.
    version_group: NamedAPIResource[VersionGroup]


@dataclass
class Name:
    # The localized name for an API resource in a specific language.
    name: str
    # The language this name is in.
    language: NamedAPIResource[Language]


@dataclass
class NamedAPIResource(Generic[T]):
    # The name of the referenced resource.
    name: str
    # The URL of the referenced resource.
    url: str


@dataclass
class VerboseEffect:
    # The localized effect text for an API resource in a specific language.
    effect: str
    # The localized effect text in brief.
    short_effect: str
    # The language this effect is in.
    language: NamedAPIResource[Language]


@dataclass
class VersionEncounterDetail:
    # The game version this encounter happens in.
    version: NamedAPIResource[Version]
    # The total percentage of all encounter potential.
    max_chance: int
    # A list of encounters and their specifics.
    encounter_details: List[Encounter]


@dataclass
class VersionGameIndex:
    # The internal id of an API resource within game data.
    game_index: int
    # The version relevent to this game index.
    version: NamedAPIResource[Version]


@dataclass
class VersionGroupFlavorText:
    # The localized name for an API resource in a specific language.
    text: str
    # The language this name is in.
    language: NamedAPIResource[Language]
    # The version group which uses this flavor text.
    version_group: NamedAPIResource[VersionGroup]
