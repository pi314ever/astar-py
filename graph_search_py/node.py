from typing import Generic, Optional

from .typing import ST


class Node(Generic[ST]):
    """Generic node class used in search algorithms."""
    def __init__(
        self,
        state: ST,
        path_cost: float,
        heuristic_cost: float,
        is_solved: bool,
        parent: Optional["Node[ST]"] = None,
    ) -> None:
        """Defines a node in a search tree. 

        @param state: The state of the node.
        @param path_cost: The cost to reach the node from the start node.
        @param heuristic_cost: The estimated cost to reach the goal node from the node.
        @param parent: The parent node of the node. Can be None if no parent exists.
        """
        self.state = state
        self.path_cost = path_cost
        self.heuristic_cost = heuristic_cost
        self.is_solved = is_solved
        self.parent = parent

        self.children = []
        self.transition_costs = []

    def __lt__(self, other: "Node[ST]") -> bool:
        return (self.path_cost + self.heuristic_cost) < (
            other.path_cost + other.heuristic_cost
        )

    def is_equal(self, other: "Node[ST]") -> bool:
        return self.state == other.state

    @property
    def cost(self) -> float:
        return self.path_cost + self.heuristic_cost * int(not self.is_solved)
