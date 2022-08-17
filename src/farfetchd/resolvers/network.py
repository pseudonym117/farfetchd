import aiohttp
import threading

from typing import List, TypeVar

# todo: clean up these imports
from ..serialization import Deserializer

from ..resources import CacheableResource, CacheableResourceList
from .resolver import Resolver

T = TypeVar("T")


class ApiResolver(Resolver):
    def __init__(self, deserializer: Deserializer) -> None:
        self.__session_lock = threading.Lock()
        self.__session: aiohttp.ClientSession | None = None
        self._deserializer = deserializer

    async def _session(self) -> aiohttp.ClientSession:
        if not self.__session:
            with self.__session_lock:
                if not self.__session:
                    self.__session = aiohttp.ClientSession()
        return self.__session

    async def resolve(
        self, to_resolve: CacheableResource[T] | CacheableResourceList[T]
    ) -> T | List[T] | None:
        session = await self._session()
        async with session.get(to_resolve.resource_url) as resp:
            data = await resp.json()

            return self._deserializer.from_dict(to_resolve.resource_type, data)
