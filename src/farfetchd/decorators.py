import functools
from typing import Callable, ParamSpec, TypeVar, Type

from .resources import CacheableResource, CacheableResourceList
from ._farfetchd import Farfetchd

T = TypeVar("T")
P = ParamSpec("P")

CachedT = CacheableResource[T] | CacheableResourceList[T]


def defines(type: Type[T]):
    def decorator(function: Callable[P, CachedT]) -> Callable[P, CachedT]:
        @functools.wraps(function)
        def decorated(*args, **kwargs):
            return function(*args, **kwargs)

        Farfetchd.definers.register(type, decorated)
        return decorated

    return decorator
