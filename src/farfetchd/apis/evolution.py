"""
!!Generated code!!

Do not modify directly.

Generation script is located @ //farfetchd/bin/generate.py
"""

# todo: rename this file, or just move class
from ..resources import (
    CacheableResource,
    CacheableResourceList,
    PaginationArguments,
    ResourceIdentifier,
)


from ..models.evolution import (
    EvolutionChain,
    EvolutionTrigger,
)


class EvolutionApi:
    def evolution_chains(
        self,
        id: int | None = None,
        pagination: PaginationArguments | None = None,
    ) -> CacheableResource[EvolutionChain] | CacheableResourceList[EvolutionChain]:
        """
        Evolution chains are essentially family trees. They start with the lowest stage within a family and detail evolution conditions for each as well as Pokemon they can evolve into up through the hierarchy.
        """

        if id is not None:
            return CacheableResource(
                EvolutionChain,
                ResourceIdentifier("id", id),
                f"https://pokeapi.co/api/v2/evolution-chain/{id}",
            )

        if pagination is not None:
            return CacheableResourceList(
                EvolutionChain, pagination, "https://pokeapi.co/api/v2/evolution-chain/"
            )
        raise ValueError("this exception should be impossible")

    def evolution_triggers(
        self,
        id: int | None = None,
        name: str | None = None,
        pagination: PaginationArguments | None = None,
    ) -> CacheableResource[EvolutionTrigger] | CacheableResourceList[EvolutionTrigger]:
        """
        Evolution triggers are the events and conditions that cause a Pokemon to evolve. Check out Bulbapedia for greater detail.
        """

        if not self._exactly_one_non_none(
            id,
            name,
            pagination,
        ):
            raise ValueError(
                "Invalid arguments; exactly one of [id, name, pagination] must not be None"
            )

        if id is not None:
            return CacheableResource(
                EvolutionTrigger,
                ResourceIdentifier("id", id),
                f"https://pokeapi.co/api/v2/evolution-trigger/{id}",
            )

        if name is not None:
            return CacheableResource(
                EvolutionTrigger,
                ResourceIdentifier("name", name),
                f"https://pokeapi.co/api/v2/evolution-trigger/{name}",
            )

        if pagination is not None:
            return CacheableResourceList(
                EvolutionTrigger,
                pagination,
                "https://pokeapi.co/api/v2/evolution-trigger/",
            )
        raise ValueError("this exception should be impossible")

    def _exactly_one_non_none(self, *args) -> bool:
        has_non_none = False
        for arg in args:
            if arg is not None:
                if has_non_none:
                    return False
                has_non_none = True
        return has_non_none
