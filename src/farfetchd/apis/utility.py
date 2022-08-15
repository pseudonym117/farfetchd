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


from ..models.utility import (
    Language,
)


class UtilityApi:
    def languages(
        self,
        id: int | None = None,
        name: str | None = None,
        pagination: PaginationArguments | None = None,
    ) -> CacheableResource[Language] | CacheableResourceList[Language]:
        """
        Languages for translations of API resource information.
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
                Language,
                ResourceIdentifier("id", id),
                f"https://pokeapi.co/api/v2/language/{id}",
            )

        if name is not None:
            return CacheableResource(
                Language,
                ResourceIdentifier("name", name),
                f"https://pokeapi.co/api/v2/language/{name}",
            )

        if pagination is not None:
            return CacheableResourceList(
                Language, pagination, "https://pokeapi.co/api/v2/language/"
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
