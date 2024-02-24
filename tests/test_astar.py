from astar_py.astar import AStar


def test_astar():
    map = [list(range(10)) for _ in range(10)]
    def expand_state_fn(state):
        x, y = state
        children = []
        costs = []
        if x > 0:
            children.append((x - 1, y))
            costs.append(map[x - 1][y])
        if x < 9:
            children.append((x + 1, y))
            costs.append(map[x + 1][y])
        if y > 0:
            children.append((x, y - 1))
            costs.append(map[x][y - 1])
        if y < 9:
            children.append((x, y + 1))
            costs.append(map[x][y + 1])
        return children, costs
    astar = AStar(
        initial_state=(0, 0),
        heuristic_fn=lambda state: abs(state[0] - 9) + abs(state[1] - 9),
        expand_state_fn=expand_state_fn,
        is_solved_fn=lambda state: state == (9, 9),
        max_steps=20,
        stop_when_solved=True,
    )

    astar.search()

