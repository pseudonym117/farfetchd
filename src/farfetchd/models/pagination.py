"""
!!Generated code!!

Do not modify directly.

Generation script is located @ //farfetchd/bin/generate.py
"""

from __future__ import annotations
from dataclasses import dataclass

from ..base import Model


from typing import Generic, Type, TypeVar

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

    # The type that this NamedAPIResourceList resolves to
    type: Type[T] | None = None


# import all type hints at of file to ensure no circular reference issues

from typing import (
    List,
)

from .utility import (
    NamedAPIResource,
)
