from typing import Generic, TypeVar, Type

from ._farfetchd import Farfetchd


T = TypeVar("T")


class ObjectManager(Generic[T]):
    def __init__(self, model_type: Type[T]) -> None:
        self._model_type = model_type

    async def get(self, **kwargs: dict[str, str | int]) -> T:
        definer = Farfetchd.definers.get(self._model_type)
        definition = definer(**kwargs)

        return await Farfetchd.resolvers.resolve(definition)


class Meta(type):
    def __new__(cls, name, bases, dct):
        response = super().__new__(cls, name, bases, dct)
        response.objects = ObjectManager(response)
        return response


class Model(Generic[T], metaclass=Meta):
    objects: ObjectManager[T]
