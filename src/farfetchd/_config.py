from .resolvers.network import ApiResolver
from .serialization import DataclassDeserializer
from ._farfetchd import Farfetchd

# import has side effects (registers all definition providers)
# should not be removed
from .defs import *


def default():
    Farfetchd.resolvers.register(-1, ApiResolver(DataclassDeserializer()))
