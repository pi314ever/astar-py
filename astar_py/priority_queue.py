from heapq import heappop, heappush
from typing import Generic, Iterable, Optional

from .node import Node
from .typing import ST


class PriorityQueue(Generic[ST]):
    """Priority queue implementation using heapq for generic nodes ordered by cost."""

    def __init__(
        self, nodes: Optional[Iterable[Node[ST]]] = None, flipped: bool = False
    ):
        self.heap: list[tuple[float, Node[ST]]] = []
        self.flipped = flipped

        # PQ is initialized, push all items to the heap
        if nodes is not None:
            for item in nodes:
                self.push(item)

    def push(self, node: Node[ST]):
        if self.flipped:
            heappush(self.heap, (-node.cost, node))
        else:
            heappush(self.heap, (node.cost, node))

    def pop(self) -> Node[ST]:
        _, node = heappop(self.heap)
        return node

    def __len__(self):
        return len(self.heap)

    def __bool__(self):
        return bool(self.heap)


class DoubleEndedPriorityQueue(Generic[ST]):
    """Double ended priority queue implementation using deque."""

    def __init__(self, nodes: Optional[Iterable[Node[ST]]] = None, max_size: int = 0):
        """
        @param nodes: Initial nodes to add to the queue.
        @param max_size: Maximum size of the queue. 0 means no limit.
        """
        pass
