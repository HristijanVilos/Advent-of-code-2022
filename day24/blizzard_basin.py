from collections import deque


def add_to_new_pos(dir, node, new_pos: dict):
    if dir == ".":
        return
    x = new_pos.get(node, ".")
    if x == ".":
        new_pos[node] = dir
    elif isinstance(x, str):
        new_pos[node] = [x, dir]
    elif isinstance(x, list):
        new_pos[node].append(dir)


def oposite_site(dir: str, node: tuple, edge_values: tuple) -> tuple:
    dir_to_move = {
        ">": (node[0], edge_values[2]),
        "<": (node[0], edge_values[3]),
        "^": (edge_values[1], node[1]),
        "v": (edge_values[0], node[1])
    }
    return dir_to_move[dir]


def move_dir_blizard(dir: str, node: tuple, grid: set, edge_values):
    if dir == ">":
        if (node[0], node[1] + 1) in grid:
            return (node[0], node[1] + 1)
        return oposite_site(dir, node, edge_values)
    elif dir == "<":
        if (node[0], node[1] - 1) in grid:
            return (node[0], node[1] - 1)
        return oposite_site(dir, node, edge_values)
    elif dir == "^":
        if (node[0] - 1, node[1]) in grid:
            return (node[0] - 1, node[1])
        return oposite_site(dir, node, edge_values)
    elif dir == "v":
        if (node[0] + 1, node[1]) in grid:
            return (node[0] + 1, node[1])
        return oposite_site(dir, node, edge_values)
    else:
        return node


def simulate_one_round_blizard(grid: set, current_pos: dict,
                               edge_values: tuple) -> dict:
    new_pos = {}
    for node in grid:
        dir = current_pos.get(node, ".")
        if isinstance(dir, str):
            new_node = move_dir_blizard(dir, node, grid, edge_values)
            add_to_new_pos(dir, new_node, new_pos)
        elif isinstance(dir, list):
            for d in dir:
                new_node = move_dir_blizard(d, node, grid, edge_values)
                add_to_new_pos(d, new_node, new_pos)
    return new_pos


def print_grid_adc_style(grid: set, pos: dict, min_j: int):
    list_grid = list(grid)
    list_grid.sort()
    result_str = ""
    for node in list_grid:
        if node[1] == min_j:
            print(result_str)
            result_str = ""
        x = pos.get(node, ".")
        if x == ".":
            result_str += "."
        elif isinstance(x, str):
            result_str += x
        else:
            result_str += str(len(x))
    print(result_str)


def parse(input_file):
    with open(input_file, "r") as file:
        grid = set()
        start_bliz = {}
        for i, line in enumerate(file):
            for j, c in enumerate(line.strip()):
                if c != "#":
                    grid.add((i, j))
                    start_bliz[(i, j)] = c
        min_ij, max_ij = min(grid), max(grid)
        i = [i[0] for i in grid]
        j = [j[1] for j in grid]
        min_i, max_i, min_j, max_j = min(i)+1, max(i)-1, min(j), max(j)
        edge_values = min_i, max_i, min_j, max_j
        return grid, start_bliz, edge_values, min_ij, max_ij


def valid_moves(current_pos: tuple, bliz_pos: dict, grid: set) -> list:
    posible_moves = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    available_moves = []
    for mv in posible_moves:
        x = current_pos[0] + mv[0]
        y = current_pos[1] + mv[1]
        if bliz_pos.get((x, y), ".") == "." and (x, y) in grid:
            available_moves.append((x, y))
    return available_moves


def shortest_path(grid, edge_values, start_pos, end_pos, blizard, minute):
    result = set()
    queue = deque()
    queue.append(start_pos)
    while True:
        if (end_pos, minute-1) in result:
            return blizard, minute
        blizard = simulate_one_round_blizard(grid, blizard, edge_values)

        test_q = deque()
        while len(queue) != 0:
            current_pos = queue.popleft()
            if (current_pos, minute) in result:
                continue
            result.add((current_pos, minute))

            # priority queue
            for move in valid_moves(current_pos, blizard, grid):
                test_q.append(move)

        if len(test_q) == 0:
            raise Exception("Something went wrong! I am stuck in infinite loop")
        minute += 1
        # asign test queue to queue for next minute
        queue = test_q


def solution(input_file, n):
    grid, blizard, edge_values, start_pos, end_pos = parse(input_file)
    minute = 0
    for i in range(n):
        if i % 2 == 0:
            sp = start_pos
            ep = end_pos
        else:
            sp = end_pos
            ep = start_pos
        blizard, minute = shortest_path(grid, edge_values, sp,
                                        ep, blizard, minute)
    minute = minute - 1
    return minute


print("Part 1:", solution("input.txt", 1))
print("Part 2:", solution("input.txt", 3))
