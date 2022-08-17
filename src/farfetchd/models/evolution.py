"""
!!Generated code!!

Do not modify directly.

Generation script is located @ //farfetchd/bin/generate.py
"""

from __future__ import annotations
from dataclasses import dataclass

from ..base import Model


@dataclass
class EvolutionChain(Model["EvolutionChain"]):
    # The identifier for this resource.
    id: int
    # The item that a Pokemon would be holding when mating that would trigger the egg hatching a baby Pokemon rather than a basic Pokemon.
    baby_trigger_item: NamedAPIResource[Item]
    # The base chain link object. Each link contains evolution details for a Pokemon in the chain. Each link references the next Pokemon in the natural evolution order.
    chain: ChainLink


@dataclass
class ChainLink(Model["ChainLink"]):
    # Whether or not this link is for a baby Pokemon. This would only ever be true on the base link.
    is_baby: bool
    # The Pokemon species at this point in the evolution chain.
    species: NamedAPIResource[PokemonSpecies]
    # All details regarding the specific details of the referenced Pokemon species evolution.
    evolution_details: List[EvolutionDetail]
    # A List of chain objects.
    evolves_to: List[ChainLink]


@dataclass
class EvolutionDetail(Model["EvolutionDetail"]):
    # The item required to cause evolution this into Pokemon species.
    item: NamedAPIResource[Item]
    # The type of event that triggers evolution into this Pokemon species.
    trigger: NamedAPIResource[EvolutionTrigger]
    # The id of the gender of the evolving Pokemon species must be in order to evolve into this Pokemon species.
    gender: int
    # The item the evolving Pokemon species must be holding during the evolution trigger event to evolve into this Pokemon species.
    held_item: NamedAPIResource[Item]
    # The move that must be known by the evolving Pokemon species during the evolution trigger event in order to evolve into this Pokemon species.
    known_move: NamedAPIResource[Move]
    # The evolving Pokemon species must know a move with this type during the evolution trigger event in order to evolve into this Pokemon species.
    known_move_type: NamedAPIResource[Type]
    # The location the evolution must be triggered at.
    location: NamedAPIResource[Location]
    # The minimum required level of the evolving Pokemon species to evolve into this Pokemon species.
    min_level: int
    # The minimum required level of happiness the evolving Pokemon species to evolve into this Pokemon species.
    min_happiness: int
    # The minimum required level of beauty the evolving Pokemon species to evolve into this Pokemon species.
    min_beauty: int
    # The minimum required level of affection the evolving Pokemon species to evolve into this Pokemon species.
    min_affection: int
    # Whether or not it must be raining in the overworld to cause evolution this Pokemon species.
    needs_overworld_rain: bool
    # The Pokemon species that must be in the players party in order for the evolving Pokemon species to evolve into this Pokemon species.
    party_species: NamedAPIResource[PokemonSpecies]
    # The player must have a Pokemon of this type in their party during the evolution trigger event in order for the evolving Pokemon species to evolve into this Pokemon species.
    party_type: NamedAPIResource[Type]
    # The required relation between the Pokemon's Attack and Defense stats. 1 means Attack > Defense. 0 means Attack = Defense. -1 means Attack < Defense.
    relative_physical_stats: int
    # The required time of day. Day or night.
    time_of_day: str
    # Pokemon species for which this one must be traded.
    trade_species: NamedAPIResource[PokemonSpecies]
    # Whether or not the 3DS needs to be turned upside-down as this Pokemon levels up.
    turn_upside_down: bool


@dataclass
class EvolutionTrigger(Model["EvolutionTrigger"]):
    # The identifier for this resource.
    id: int
    # The name for this resource.
    name: str
    # The name of this resource listed in different languages.
    names: List[Name]
    # A list of pokemon species that result from this evolution trigger.
    pokemon_species: List[NamedAPIResource[PokemonSpecies]]


# import all type hints at of file to ensure no circular reference issues

from typing import (
    List,
)

from .items import (
    Item,
)

from .locations import (
    Location,
)

from .moves import (
    Move,
)

from .pokemon import (
    PokemonSpecies,
    Type,
)

from .utility import (
    Name,
    NamedAPIResource,
)
