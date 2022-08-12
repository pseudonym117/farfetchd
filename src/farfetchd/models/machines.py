"""
!!Generated code!!

Do not modify directly.

Generation script is located @ //farfetchd/bin/generate.py
"""

from __future__ import annotations
from dataclasses import dataclass


from .games import (
    VersionGroup,
)

from .items import (
    Item,
)

from .moves import (
    Move,
)

from .utility import (
    NamedAPIResource,
)


@dataclass
class Machine:
    # The identifier for this resource.
    id: int
    # The TM or HM item that corresponds to this machine.
    item: NamedAPIResource[Item]
    # The move that is taught by this machine.
    move: NamedAPIResource[Move]
    # The version group that this machine applies to.
    version_group: NamedAPIResource[VersionGroup]
