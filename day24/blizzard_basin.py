def add_to_new_pos(dir, node, new_pos: dict):
    if dir == ".":
        return
    x = new_pos.get(node, ".")
    if x == ".":
        new_pos[node] = dir
    elif isinstance(x, str):
        new_pos[node] = [x, dir]
    elif isinstance(x, list):
        new_pos[node].append(x)


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


def simulate_one_round_blizard(grid: set, current_pos: dict, edge_values: tuple):
    new_pos = {}
    for node in grid:
        dir = current_pos[node]
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


def parse():
    with open("test_input.txt", "r") as file:
        grid = set()
        start_pos = {}
        for i, line in enumerate(file):
            for j, c in enumerate(line.strip()):
                if c != "#":
                    grid.add((i, j))
                    start_pos[(i, j)] = c
        min_ij, max_ij = min(grid), max(grid)
        grid.remove(min_ij)
        grid.remove(max_ij)
        i = [i[0] for i in grid]
        j = [j[1] for j in grid]
        min_i, max_i = min(i), max(i)
        min_j, max_j = min(j), max(j)
        edge_values = min_i, max_i, min_j, max_j
        start_pos[min_ij], start_pos[max_ij] = "S", "E"
        return grid, start_pos, edge_values


def part_1():
    grid, start_pos, edge_values = parse()
    new_pos = simulate_one_round_blizard(grid, start_pos, edge_values)
    print_grid_adc_style(grid, new_pos, edge_values[2])


print("Part 1:", part_1())
