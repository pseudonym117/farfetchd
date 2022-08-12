"""
!!Generated code!!

Do not modify directly.

Generation script is located @ //farfetchd/bin/generate.py
"""

from __future__ import annotations
from dataclasses import dataclass


from typing import (
    List,
)

from .berries import (
    BerryFlavor,
)

from .moves import (
    Move,
)

from .utility import (
    Effect,
    FlavorText,
    Language,
    NamedAPIResource,
)


@dataclass
class ContestType:
    # The identifier for this resource.
    id: int
    # The name for this resource.
    name: str
    # The berry flavor that correlates with this contest type.
    berry_flavor: NamedAPIResource[BerryFlavor]
    # The name of this contest type listed in different languages.
    names: List[ContestName]


@dataclass
class ContestName:
    # The name for this contest.
    name: str
    # The color associated with this contest's name.
    color: str
    # The language that this name is in.
    language: NamedAPIResource[Language]


@dataclass
class ContestEffect:
    # The identifier for this resource.
    id: int
    # The base number of hearts the user of this move gets.
    appeal: int
    # The base number of hearts the user's opponent loses.
    jam: int
    # The result of this contest effect listed in different languages.
    effect_entries: List[Effect]
    # The flavor text of this contest effect listed in different languages.
    flavor_text_entries: List[FlavorText]


@dataclass
class SuperContestEffect:
    # The identifier for this resource.
    id: int
    # The level of appeal this super contest effect has.
    appeal: int
    # The flavor text of this super contest effect listed in different languages.
    flavor_text_entries: List[FlavorText]
    # A list of moves that have the effect when used in super contests.
    moves: List[NamedAPIResource[Move]]
