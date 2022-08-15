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

from .utility import (
    NamedAPIResource,
)


T = TypeVar("T")


@dataclass
class NamedAPIResourceList(Generic[T]):
    # The total number of resources available from this API.
    count: int
    # The URL for the next page in the list.
    next: str
    # The URL for the previous page in the list.
    previous: str
    # A list of named API resources.
    results: List[NamedAPIResource]
