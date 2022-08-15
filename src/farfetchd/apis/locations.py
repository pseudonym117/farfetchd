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


from ..models.locations import (
    Location,
    LocationArea,
    PalParkArea,
    Region,
)


class LocationsApi:
    def locations(
        self,
        id: int | None = None,
        name: str | None = None,
        pagination: PaginationArguments | None = None,
    ) -> CacheableResource[Location] | CacheableResourceList[Location]:
        """
        Locations that can be visited within the games. Locations make up sizable portions of regions, like cities or routes.
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
                Location,
                ResourceIdentifier("id", id),
                f"https://pokeapi.co/api/v2/location/{id}",
            )

        if name is not None:
            return CacheableResource(
                Location,
                ResourceIdentifier("name", name),
                f"https://pokeapi.co/api/v2/location/{name}",
            )

        if pagination is not None:
            return CacheableResourceList(
                Location, pagination, "https://pokeapi.co/api/v2/location/"
            )
        raise ValueError("this exception should be impossible")

    def location_areas(
        self,
        id: int | None = None,
        name: str | None = None,
        pagination: PaginationArguments | None = None,
    ) -> CacheableResource[LocationArea] | CacheableResourceList[LocationArea]:
        """
        Location areas are sections of areas, such as floors in a building or cave. Each area has its own set of possible Pokemon encounters.
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
                LocationArea,
                ResourceIdentifier("id", id),
                f"https://pokeapi.co/api/v2/location-area/{id}",
            )

        if name is not None:
            return CacheableResource(
                LocationArea,
                ResourceIdentifier("name", name),
                f"https://pokeapi.co/api/v2/location-area/{name}",
            )

        if pagination is not None:
            return CacheableResourceList(
                LocationArea, pagination, "https://pokeapi.co/api/v2/location-area/"
            )
        raise ValueError("this exception should be impossible")

    def pal_park_areas(
        self,
        id: int | None = None,
        name: str | None = None,
        pagination: PaginationArguments | None = None,
    ) -> CacheableResource[PalParkArea] | CacheableResourceList[PalParkArea]:
        """
        Areas used for grouping Pokemon encounters in Pal Park. They're like habitats that are specific to Pal Park.
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
                PalParkArea,
                ResourceIdentifier("id", id),
                f"https://pokeapi.co/api/v2/pal-park-area/{id}",
            )

        if name is not None:
            return CacheableResource(
                PalParkArea,
                ResourceIdentifier("name", name),
                f"https://pokeapi.co/api/v2/pal-park-area/{name}",
            )

        if pagination is not None:
            return CacheableResourceList(
                PalParkArea, pagination, "https://pokeapi.co/api/v2/pal-park-area/"
            )
        raise ValueError("this exception should be impossible")

    def regions(
        self,
        id: int | None = None,
        name: str | None = None,
        pagination: PaginationArguments | None = None,
    ) -> CacheableResource[Region] | CacheableResourceList[Region]:
        """
        A region is an organized area of the Pokemon world. Most often, the main difference between regions is the species of Pokemon that can be encountered within them.
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
                Region,
                ResourceIdentifier("id", id),
                f"https://pokeapi.co/api/v2/region/{id}",
            )

        if name is not None:
            return CacheableResource(
                Region,
                ResourceIdentifier("name", name),
                f"https://pokeapi.co/api/v2/region/{name}",
            )

        if pagination is not None:
            return CacheableResourceList(
                Region, pagination, "https://pokeapi.co/api/v2/region/"
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