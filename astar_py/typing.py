from typing import TYPE_CHECKING, Generic, Hashable, Protocol, TypeVar

if TYPE_CHECKING:
    from .node import Node


ST = TypeVar("ST", bound=Hashable)  # State type

class PQType(Protocol, Generic[ST]):
    def push(self, node: "Node[ST]") -> None: ...
    def pop(self) -> "Node[ST]": ...
    def __len__(self) -> int: ...
