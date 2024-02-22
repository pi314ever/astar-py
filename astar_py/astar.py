from logging import getLogger
from typing import Callable, Generic, List, Optional, Tuple

from .node import Node
from .priority_queue import PriorityQueue
from .typing import ST, PQType

logger = getLogger(__name__)

if logger.level <= 10:
    logger.debug("astar.py loaded")

__all__ = ["AStar"]


class AStar(Generic[ST]):
    """A* search algorithm."""

    def __init__(
        self,
        initial_state: ST,
        heuristic_fn: Callable[[ST], float],
        expand_state_fn: Callable[[ST], Tuple[List[ST], List[float]]],
        is_solved_fn: Callable[[ST], bool],
        goal_state: Optional[ST] = None,
        stop_at_goal: bool = True,
        max_steps: int = 1000,
        frontier: Optional[PQType] = None,
    ) -> None:
        """Initializes the A* search algorithm.

        @param initial_state: The initial state of the search.
        @param heuristic_fn: The heuristic function to estimate the cost to reach the goal state from a given state.
        @param expand_state_fn: The function to expand a state into its children states with the associated transition costs.
        @param is_solved_fn: The function to check if a state is the goal state.
        @param goal_state: The goal state of the search.
        @param stop_at_goal: If True, the search stops when the goal state is found.
        @param max_steps: The maximum number of steps to run in the search.
        @param frontier: The priority queue to use for the frontier. The priority queue is responsible for managing the maximum queue sizes. If None, a default priority queue is used.
        """

        if frontier is None:
            frontier = PriorityQueue()
        self.frontier: PQType = frontier
        self.explored: dict[ST, float] = {}  # Map from state to minimum path cost
        self.heuristic_fn = heuristic_fn
        self.expand_state_fn = expand_state_fn
        self.is_solved_fn = is_solved_fn
        self._steps = 0
        self.max_steps = max_steps
        self.solutions: list[Node] = []

        # Parse first node
        initial_node = Node(
            initial_state, 0, heuristic_fn(initial_state), is_solved_fn(initial_state)
        )
        self.frontier.push(initial_node)

    def step(self):
        """Executes one step of the A* search algorithm."""

        # Pop node from frontier
        if len(self.frontier) <= 0:
            logger.error("No more nodes in the frontier")
            return

        # Calculate neighbors
        parent_node = self.frontier.pop()
        states_children, transition_costs_children = self.expand_state_fn(
            parent_node.state
        )
        heuristics_children = [self.heuristic_fn(s) for s in states_children]
        is_solved_children = [self.is_solved_fn(s) for s in states_children]

        # Create new nodes
        new_nodes = [
            Node(
                state=state,
                path_cost=parent_node.path_cost + tc,
                heuristic_cost=heur,
                is_solved=is_solved,
                parent=parent_node,
            )
            for state, tc, heur, is_solved in zip(
                states_children,
                transition_costs_children,
                heuristics_children,
                is_solved_children,
            )
        ]

        # Update explored and remove duplicates
        new_nodes = self._explore(new_nodes)

        # Add new nodes to frontier
        for node in new_nodes:
            self.frontier.push(node)

        self._steps += 1

    def _explore(self, nodes: List[Node]):
        """Explores the nodes and returns nodes not already explored."""
        not_explored = []
        for node in nodes:
            if node.state in self.explored:
                if self.explored[node.state] <= node.path_cost:
                    continue
            self.explored[node.state] = node.path_cost
            not_explored.append(node)
        return not_explored

    def search(self):
        """Runs the A* search to completion."""
        while len(self.frontier) > 0 and self._steps < self.max_steps:
            self.step()
