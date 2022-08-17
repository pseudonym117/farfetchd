import abc

from typing import List, TypeVar

from ..resources import CacheableResource, CacheableResourceList


T = TypeVar("T")


class Resolver(abc.ABC):
    @abc.abstractmethod
    async def resolve(
        self, to_resolve: CacheableResource[T] | CacheableResourceList[T]
    ) -> T | List[T] | None:
        raise NotImplementedError()

    async def store(self, to_store: T | List[T]):
        pass
