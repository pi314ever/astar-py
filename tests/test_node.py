import pytest

from astar_py.node import Node

@pytest.fixture
def node():
    return Node(tuple(range(5)), 0.0, 1.0, False)

def test_node_creation(node: "Node[tuple[int,...]]"):
    assert node.state == (0, 1, 2, 3, 4), "Node state is not correct"
    assert node.path_cost == 0.0, "Node path cost not set correctly"
    assert node.heuristic_cost == 1.0, "Node heuristic cost not set correctly"
    assert node.is_solved == False, "Node solved not set correctly"
    assert node.cost == 1.0, "Node cost is not calculated properly"

    node.is_solved = True
    assert node.cost == 0.0, "Node cost for solved states is not calculated properly"

    assert node.parent == None, "Node parent not set correctly"
    assert node.children == [], "Node children not set correctly"

def test_node_comparision(node: "Node[tuple[int,...]]"):
    node_2 = Node(tuple(range(5)), 0.0, 1.5, False)
    assert node.is_equal(node_2), "Node comparision equality failed"

    node_3 = Node(tuple(range(5)), 0.0, 2.0, False)
    assert node < node_3, "Node comparision less than failed"

    nodes_list = sorted([node_3, node_2, node])
    assert nodes_list == [node, node_2, node_3], "Node comparision sorting failed"
