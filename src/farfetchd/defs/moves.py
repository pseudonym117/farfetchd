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


from ..models.moves import (
    Move,
    MoveAilment,
    MoveBattleStyle,
    MoveCategory,
    MoveDamageClass,
    MoveLearnMethod,
    MoveTarget,
)


@defines(Move)
def moves(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[Move] | CacheableResourceList[Move]:
    """
    Moves are the skills of Pokemon in battle. In battle, a Pokemon uses one move each turn. Some moves (including those learned by Hidden Machine) can be used outside of battle as well, usually for the purpose of removing obstacles or exploring new areas.
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
            Move, ResourceIdentifier("id", id), f"https://pokeapi.co/api/v2/move/{id}"
        )

    if name is not None:
        return CacheableResource(
            Move,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/move/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            Move, pagination, "https://pokeapi.co/api/v2/move/"
        )
    raise ValueError("this exception should be impossible")


@defines(MoveAilment)
def move_ailments(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[MoveAilment] | CacheableResourceList[MoveAilment]:
    """
    Move Ailments are status conditions caused by moves used during battle. See Bulbapedia for greater detail.
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
            MoveAilment,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/move-ailment/{id}",
        )

    if name is not None:
        return CacheableResource(
            MoveAilment,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/move-ailment/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            MoveAilment, pagination, "https://pokeapi.co/api/v2/move-ailment/"
        )
    raise ValueError("this exception should be impossible")


@defines(MoveBattleStyle)
def move_battle_styles(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[MoveBattleStyle] | CacheableResourceList[MoveBattleStyle]:
    """
    Styles of moves when used in the Battle Palace. See Bulbapedia for greater detail.
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
            MoveBattleStyle,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/move-battle-style/{id}",
        )

    if name is not None:
        return CacheableResource(
            MoveBattleStyle,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/move-battle-style/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            MoveBattleStyle, pagination, "https://pokeapi.co/api/v2/move-battle-style/"
        )
    raise ValueError("this exception should be impossible")


@defines(MoveCategory)
def move_categories(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[MoveCategory] | CacheableResourceList[MoveCategory]:
    """
    Very general categories that loosely group move effects.
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
            MoveCategory,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/move-category/{id}",
        )

    if name is not None:
        return CacheableResource(
            MoveCategory,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/move-category/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            MoveCategory, pagination, "https://pokeapi.co/api/v2/move-category/"
        )
    raise ValueError("this exception should be impossible")


@defines(MoveDamageClass)
def move_damage_classes(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[MoveDamageClass] | CacheableResourceList[MoveDamageClass]:
    """
    Damage classes moves can have, e.g. physical, special, or non-damaging.
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
            MoveDamageClass,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/move-damage-class/{id}",
        )

    if name is not None:
        return CacheableResource(
            MoveDamageClass,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/move-damage-class/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            MoveDamageClass, pagination, "https://pokeapi.co/api/v2/move-damage-class/"
        )
    raise ValueError("this exception should be impossible")


@defines(MoveLearnMethod)
def move_learn_methods(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[MoveLearnMethod] | CacheableResourceList[MoveLearnMethod]:
    """
    Methods by which Pokemon can learn moves.
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
            MoveLearnMethod,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/move-learn-method/{id}",
        )

    if name is not None:
        return CacheableResource(
            MoveLearnMethod,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/move-learn-method/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            MoveLearnMethod, pagination, "https://pokeapi.co/api/v2/move-learn-method/"
        )
    raise ValueError("this exception should be impossible")


@defines(MoveTarget)
def move_targets(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[MoveTarget] | CacheableResourceList[MoveTarget]:
    """
    Targets moves can be directed at during battle. Targets can be Pokemon, environments or even other moves.
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
            MoveTarget,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/move-target/{id}",
        )

    if name is not None:
        return CacheableResource(
            MoveTarget,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/move-target/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            MoveTarget, pagination, "https://pokeapi.co/api/v2/move-target/"
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