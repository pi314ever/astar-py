from abc import abstractmethod
from typing import TYPE_CHECKING, Generic, Hashable, Protocol, TypeVar

if TYPE_CHECKING:
    from .node import Node


ST = TypeVar("ST", bound=Hashable)  # State type
AT = TypeVar("AT")  # Action type

class PQType(Protocol, Generic[ST, AT]):
    def push(self, node: "Node[ST, AT]") -> None: ...
    def pop(self) -> "Node[ST, AT]": ...
    def __len__(self) -> int: ...
