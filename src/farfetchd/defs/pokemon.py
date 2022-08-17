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


from ..models.pokemon import (
    Ability,
    Characteristic,
    EggGroup,
    Gender,
    GrowthRate,
    LocationAreaEncounter,
    Nature,
    PokeathlonStat,
    Pokemon,
    PokemonColor,
    PokemonForm,
    PokemonHabitat,
    PokemonShape,
    PokemonSpecies,
    Stat,
    Type,
)


@defines(Ability)
def abilities(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[Ability] | CacheableResourceList[Ability]:
    """
    Abilities provide passive effects for Pokemon in battle or in the overworld. Pokemon have multiple possible abilities but can have only one ability at a time. Check out Bulbapedia for greater detail.
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
            Ability,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/ability/{id}",
        )

    if name is not None:
        return CacheableResource(
            Ability,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/ability/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            Ability, pagination, "https://pokeapi.co/api/v2/ability/"
        )
    raise ValueError("this exception should be impossible")


@defines(Characteristic)
def characteristics(
    id: int | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[Characteristic] | CacheableResourceList[Characteristic]:
    """
    Characteristics indicate which stat contains a Pokemon's highest IV. A Pokemon's Characteristic is determined by the remainder of its highest IV divided by 5 (gene_modulo). Check out Bulbapedia for greater detail.
    """

    if id is not None:
        return CacheableResource(
            Characteristic,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/characteristic/{id}",
        )

    if pagination is not None:
        return CacheableResourceList(
            Characteristic, pagination, "https://pokeapi.co/api/v2/characteristic/"
        )
    raise ValueError("this exception should be impossible")


@defines(EggGroup)
def egg_groups(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[EggGroup] | CacheableResourceList[EggGroup]:
    """
    Egg Groups are categories which determine which Pokemon are able to interbreed. Pokemon may belong to either one or two Egg Groups. Check out Bulbapedia for greater detail.
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
            EggGroup,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/egg-group/{id}",
        )

    if name is not None:
        return CacheableResource(
            EggGroup,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/egg-group/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            EggGroup, pagination, "https://pokeapi.co/api/v2/egg-group/"
        )
    raise ValueError("this exception should be impossible")


@defines(Gender)
def genders(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[Gender] | CacheableResourceList[Gender]:
    """
    Genders were introduced in Generation II for the purposes of breeding Pokemon but can also result in visual differences or even different evolutionary lines. Check out Bulbapedia for greater detail.
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
            Gender,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/gender/{id}",
        )

    if name is not None:
        return CacheableResource(
            Gender,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/gender/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            Gender, pagination, "https://pokeapi.co/api/v2/gender/"
        )
    raise ValueError("this exception should be impossible")


@defines(GrowthRate)
def growth_rates(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[GrowthRate] | CacheableResourceList[GrowthRate]:
    """
    Growth rates are the speed with which Pokemon gain levels through experience. Check out Bulbapedia for greater detail.
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
            GrowthRate,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/growth-rate/{id}",
        )

    if name is not None:
        return CacheableResource(
            GrowthRate,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/growth-rate/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            GrowthRate, pagination, "https://pokeapi.co/api/v2/growth-rate/"
        )
    raise ValueError("this exception should be impossible")


@defines(Nature)
def natures(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[Nature] | CacheableResourceList[Nature]:
    """
    Natures influence how a Pokemon's stats grow. See Bulbapedia for greater detail.
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
            Nature,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/nature/{id}",
        )

    if name is not None:
        return CacheableResource(
            Nature,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/nature/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            Nature, pagination, "https://pokeapi.co/api/v2/nature/"
        )
    raise ValueError("this exception should be impossible")


@defines(PokeathlonStat)
def pokeathlon_stats(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[PokeathlonStat] | CacheableResourceList[PokeathlonStat]:
    """
    Pokeathlon Stats are different attributes of a Pokemon's performance in Pokeathlons. In Pokeathlons, competitions happen on different courses; one for each of the different Pokeathlon stats. See Bulbapedia for greater detail.
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
            PokeathlonStat,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/pokeathlon-stat/{id}",
        )

    if name is not None:
        return CacheableResource(
            PokeathlonStat,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/pokeathlon-stat/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            PokeathlonStat, pagination, "https://pokeapi.co/api/v2/pokeathlon-stat/"
        )
    raise ValueError("this exception should be impossible")


@defines(Pokemon)
def pokemon(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[Pokemon] | CacheableResourceList[Pokemon]:
    """
    Pokemon are the creatures that inhabit the world of the Pokemon games. They can be caught using Pokeballs and trained by battling with other Pokemon.  Each Pokemon belongs to a specific species but may take on a variant which makes it differ from other Pokemon of the same species, such as base stats, available abilities and typings. See Bulbapedia for greater detail.
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
            Pokemon,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/pokemon/{id}",
        )

    if name is not None:
        return CacheableResource(
            Pokemon,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/pokemon/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            Pokemon, pagination, "https://pokeapi.co/api/v2/pokemon/"
        )
    raise ValueError("this exception should be impossible")


@defines(LocationAreaEncounter)
def pokemon_location_areas(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[LocationAreaEncounter] | CacheableResourceList[
    LocationAreaEncounter
]:
    """
    Pokemon Location Areas are ares where Pokemon can be found.
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
            LocationAreaEncounter,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/pokemon/{id}",
        )

    if name is not None:
        return CacheableResource(
            LocationAreaEncounter,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/pokemon/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            LocationAreaEncounter, pagination, "https://pokeapi.co/api/v2/pokemon/"
        )
    raise ValueError("this exception should be impossible")


@defines(PokemonColor)
def pokemon_colors(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[PokemonColor] | CacheableResourceList[PokemonColor]:
    """
    Colors used for sorting Pokemon in a Pokedex. The color listed in the Pokedex is usually the color most apparent or covering each Pokemon's body. No orange category exists; Pokemon that are primarily orange are listed as red or brown.
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
            PokemonColor,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/pokemon-color/{id}",
        )

    if name is not None:
        return CacheableResource(
            PokemonColor,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/pokemon-color/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            PokemonColor, pagination, "https://pokeapi.co/api/v2/pokemon-color/"
        )
    raise ValueError("this exception should be impossible")


@defines(PokemonForm)
def pokemon_forms(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[PokemonForm] | CacheableResourceList[PokemonForm]:
    """
    Some Pokemon may appear in one of multiple, visually different forms. These differences are purely cosmetic. For variations within a Pokemon species, which do differ in more than just visuals, the 'Pokemon' entity is used to represent such a variety.
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
            PokemonForm,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/pokemon-form/{id}",
        )

    if name is not None:
        return CacheableResource(
            PokemonForm,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/pokemon-form/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            PokemonForm, pagination, "https://pokeapi.co/api/v2/pokemon-form/"
        )
    raise ValueError("this exception should be impossible")


@defines(PokemonHabitat)
def pokemon_habitats(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[PokemonHabitat] | CacheableResourceList[PokemonHabitat]:
    """
    Habitats are generally different terrain Pokemon can be found in but can also be areas designated for rare or legendary Pokemon.
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
            PokemonHabitat,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/pokemon-habitat/{id}",
        )

    if name is not None:
        return CacheableResource(
            PokemonHabitat,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/pokemon-habitat/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            PokemonHabitat, pagination, "https://pokeapi.co/api/v2/pokemon-habitat/"
        )
    raise ValueError("this exception should be impossible")


@defines(PokemonShape)
def pokemon_shapes(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[PokemonShape] | CacheableResourceList[PokemonShape]:
    """
    Shapes used for sorting Pokemon in a Pokedex.
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
            PokemonShape,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/pokemon-shape/{id}",
        )

    if name is not None:
        return CacheableResource(
            PokemonShape,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/pokemon-shape/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            PokemonShape, pagination, "https://pokeapi.co/api/v2/pokemon-shape/"
        )
    raise ValueError("this exception should be impossible")


@defines(PokemonSpecies)
def pokemon_species(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[PokemonSpecies] | CacheableResourceList[PokemonSpecies]:
    """
    A Pokemon Species forms the basis for at least one Pokemon. Attributes of a Pokemon species are shared across all varieties of Pokemon within the species. A good example is Wormadam; Wormadam is the species which can be found in three different varieties, Wormadam-Trash, Wormadam-Sandy and Wormadam-Plant.
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
            PokemonSpecies,
            ResourceIdentifier("id", id),
            f"https://pokeapi.co/api/v2/pokemon-species/{id}",
        )

    if name is not None:
        return CacheableResource(
            PokemonSpecies,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/pokemon-species/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            PokemonSpecies, pagination, "https://pokeapi.co/api/v2/pokemon-species/"
        )
    raise ValueError("this exception should be impossible")


@defines(Stat)
def stats(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[Stat] | CacheableResourceList[Stat]:
    """
    Stats determine certain aspects of battles. Each Pokemon has a value for each stat which grows as they gain levels and can be altered momentarily by effects in battles.
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
            Stat, ResourceIdentifier("id", id), f"https://pokeapi.co/api/v2/stat/{id}"
        )

    if name is not None:
        return CacheableResource(
            Stat,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/stat/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            Stat, pagination, "https://pokeapi.co/api/v2/stat/"
        )
    raise ValueError("this exception should be impossible")


@defines(Type)
def types(
    id: int | None = None,
    name: str | None = None,
    pagination: PaginationArguments | None = None,
) -> CacheableResource[Type] | CacheableResourceList[Type]:
    """
    Types are properties for Pokemon and their moves. Each type has three properties: which types of Pokemon it is super effective against, which types of Pokemon it is not very effective against, and which types of Pokemon it is completely ineffective against.
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
            Type, ResourceIdentifier("id", id), f"https://pokeapi.co/api/v2/type/{id}"
        )

    if name is not None:
        return CacheableResource(
            Type,
            ResourceIdentifier("name", name),
            f"https://pokeapi.co/api/v2/type/{name}",
        )

    if pagination is not None:
        return CacheableResourceList(
            Type, pagination, "https://pokeapi.co/api/v2/type/"
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
