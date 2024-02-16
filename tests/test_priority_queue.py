from astar_py.priority_queue import PriorityQueue, DoubleEndedPriorityQueue
from astar_py.node import Node

def test_priority_queue():
    pq = PriorityQueue()

    nodes = [Node(str(i), i, i, False) for i in range(10)]
    for node in nodes:
        pq.push(node)
    
    assert len(pq) == 10, "Initial length of queue is not correct"
    for i in range(10):
        node = pq.pop()
        assert node.state == str(i)
        assert node.path_cost == i
        assert node.cost == 2 * i
    assert len(pq) == 0

# def test_double_ended_priority_queue():
#     pq = DoubleEndedPriorityQueue()
#
#     nodes = [Node(str(i), i, i, False) for i in range(10)]
#     for i in range(10):
#         pq.push(nodes[i])
#
#     assert len(pq) == 10, "Initial length of queue is not correct"
#     assert len(pq.min_heap) == 5, "Initial length of min heap is not correct"
#     assert len(pq.max_heap) == 5, "Initial length of max heap is not correct"
#
#     # 
#     for i in range(10):
#         cost, node = pq.pop_min()
#         assert cost == i
#         assert node.state == str(i)
