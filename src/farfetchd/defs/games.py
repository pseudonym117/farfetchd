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


from ..models.games import (
    Generation,
    Pokedex,
    Version,
    VersionGroup,
)


@defines(Generation)
def generations(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[Generation] | CacheableResourceList[Generation]:
    """
    A generation is a grouping of the Pokemon games that separates them based on the Pokemon they include. In each generation, a new set of Pokemon, Moves, Abilities and Types that did not exist in the previous generation are released.
    """

    if not _exactly_one_non_none(
        id,
        name,
        pagination,
    ):
        raise ValueError(
            "Invalid arguments; exactly one of [id, name, pagination] must not be None"
        )

    if id is not None:
        return CacheableResource(
            Generation,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/generation/{id}",
        )

    if name is not None:
        return CacheableResource(
            Generation,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/generation/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            Generation, pagination, "https://pokeapi.co/api/v2/generation/"
        )
    raise ValueError("this exception should be impossible")


@defines(Pokedex)
def pokedexes(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[Pokedex] | CacheableResourceList[Pokedex]:
    """
    A Pokedex is a handheld electronic encyclopedia device; one which is capable of recording and retaining information of the various Pokemon in a given region with the exception of the national dex and some smaller dexes related to portions of a region. See Bulbapedia for greater detail.
    """

    if not _exactly_one_non_none(
        id,
        name,
        pagination,
    ):
        raise ValueError(
            "Invalid arguments; exactly one of [id, name, pagination] must not be None"
        )

    if id is not None:
        return CacheableResource(
            Pokedex,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/pokedex/{id}",
        )

    if name is not None:
        return CacheableResource(
            Pokedex,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/pokedex/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            Pokedex, pagination, "https://pokeapi.co/api/v2/pokedex/"
        )
    raise ValueError("this exception should be impossible")


@defines(Version)
def version(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[Version] | CacheableResourceList[Version]:
    """
    Versions of the games, e.g., Red, Blue or Yellow.
    """

    if not _exactly_one_non_none(
        id,
        name,
        pagination,
    ):
        raise ValueError(
            "Invalid arguments; exactly one of [id, name, pagination] must not be None"
        )

    if id is not None:
        return CacheableResource(
            Version,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/version/{id}",
        )

    if name is not None:
        return CacheableResource(
            Version,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/version/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            Version, pagination, "https://pokeapi.co/api/v2/version/"
        )
    raise ValueError("this exception should be impossible")


@defines(VersionGroup)
def version_groups(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[VersionGroup] | CacheableResourceList[VersionGroup]:
    """
    Version groups categorize highly similar versions of the games.
    """

    if not _exactly_one_non_none(
        id,
        name,
        pagination,
    ):
        raise ValueError(
            "Invalid arguments; exactly one of [id, name, pagination] must not be None"
        )

    if id is not None:
        return CacheableResource(
            VersionGroup,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/version-group/{id}",
        )

    if name is not None:
        return CacheableResource(
            VersionGroup,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/version-group/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            VersionGroup, pagination, "https://pokeapi.co/api/v2/version-group/"
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
