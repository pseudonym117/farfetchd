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

from .utility import (
    Name,
    NamedAPIResource,
)


@dataclass
class EncounterMethod:
    # The identifier for this resource.
    id: int
    # The name for this resource.
    name: str
    # A good value for sorting.
    order: int
    # The name of this resource listed in different languages.
    names: List[Name]


@dataclass
class EncounterCondition:
    # The identifier for this resource.
    id: int
    # The name for this resource.
    name: str
    # The name of this resource listed in different languages.
    names: List[Name]
    # A list of possible values for this encounter condition.
    values: List[NamedAPIResource[EncounterConditionValue]]


@dataclass
class EncounterConditionValue:
    # The identifier for this resource.
    id: int
    # The name for this resource.
    name: str
    # The condition this encounter condition value pertains to.
    condition: NamedAPIResource[EncounterCondition]
    # The name of this resource listed in different languages.
    names: List[Name]
