"""
!!Generated code!!

Do not modify directly.

Generation script is located @ //farfetchd/bin/generate.py
"""

# todo: rename this file, or just move class
from ..decorators import defines
from ..resources import (
    CacheableResource,
    CacheableResourceList,
    PaginationArguments,
    ResourceIdentifier,
)


from ..models.machines import (
    Machine,
)


@defines(Machine)
def machines(
    id: int | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[Machine] | CacheableResourceList[Machine]:
    """
    Machines are the representation of items that teach moves to Pokemon. They vary from version to version, so it is not certain that one specific TM or HM corresponds to a single Machine.
    """

    if id is not None:
        return CacheableResource(
            Machine,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/machine/{id}",
        )

    if pagination is not None:
        return CacheableResourceList(
            Machine, pagination, "https://pokeapi.co/api/v2/machine/"
        )
    raise ValueError("this exception should be impossible")


def _exactly_one_non_none(*args) -> bool:
    has_non_none = False
    for arg in args:
        if arg is not None:
            if has_non_none:
                return False
            has_non_none = True
    return has_non_none
