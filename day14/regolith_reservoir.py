import re


def parse_file():
    with open("input.txt", "r") as file:
        cave = {}
        max_w = 0
        min_w = 1_000_000
        depth = 0
        for line in file:
            parsed_str = [int(_) for _ in re.findall(r'\d+', line.strip())]
            find_rocks(cave, parsed_str)
            max_w, min_w, depth =\
                find_cave_width(parsed_str, max_w, min_w, depth)
        return cave, max_w, min_w, depth


def find_cave_width(parsed_str: list, max_w, min_w, depth):
    _max_w = max([_ for i, _ in enumerate(parsed_str) if i % 2 == 0])
    _min_w = min([_ for i, _ in enumerate(parsed_str) if i % 2 == 0])
    _depth = max([0 if i % 2 == 0 else _ for i, _ in enumerate(parsed_str)])
    if _depth > depth:
        depth = _depth
    if _max_w > max_w:
        max_w = _max_w
    if _min_w < min_w:
        min_w = _min_w
    return max_w, min_w, depth


def find_air(cave, max_w, min_w, depth):
    for i in range(depth+1):
        for j in range(min_w, max_w+1, 1):
            if cave.get((i, j)) is None:
                cave[(i, j)] = "."


def find_rocks(cave: dict, parsed_str: list):
    par = []
    for i, num in enumerate(parsed_str):
        if i % 2 == 0:
            x = num
        else:
            y = num
            par.append((x, y))
    x = (par[0])
    for p in par:
        if x[0] - p[0] != 0:
            for _ in range(min(x[0], p[0]), max(x[0], p[0])+1, 1):
                cave[(p[1], _)] = "#"
        elif x[1] - p[1] != 0:
            for _ in range(min(x[1], p[1]), max(x[1], p[1])+1, 1):
                cave[(_, p[0])] = "#"
        x = p


def draw_cave(cave: dict, max_w, min_w, depth):
    for i in range(depth+1):
        print_list = []
        for j in range(min_w, max_w+1, 1):
            print_list.append(cave[i, j])
        print("".join(print_list))


def simulate_falling_send(cave, max_w, min_w, depth):
    out_of_bounds = True
    cur_pos = (0, 500)
    result = 0
    while out_of_bounds:
        cur_pos, result = falling_down(cave, result, *cur_pos)
        if cur_pos is None:
            out_of_bounds = False
    draw_cave(cave, max_w, min_w, depth)
    return result


def falling_down(cave: dict, result, i, j):
    if cave.get((i, j)) == "+":
        return None, result
    elif cave.get((i+1, j)) == ".":
        return (i+1, j), result
    elif cave.get((i+1, j)) == "#" or cave.get((i+1, j)) == "+":
        if can_move_diagonally_left(cave, i, j):
            return ((i+1, j-1)), result
        elif can_move_diagonally_right(cave, i, j):
            return ((i+1, j+1)), result
        cave[(i, j)] = "+"
        result += 1
        return (0, 500), result
    return None, result


def can_move_diagonally_left(cave: dict, i, j):
    return True if cave[i+1, j-1] == "." else False


def can_move_diagonally_right(cave: dict, i, j):
    return True if cave.get((i+1, j+1)) == "." else False


def create_floor(cave: dict, max_w, min_w, depth):
    for i in range(min_w, max_w, 1):
        cave[(depth, i)] = "#"


def part_1():
    cave, max_w, min_w, depth = parse_file()
    find_air(cave, max_w, min_w, depth)
    return simulate_falling_send(cave, max_w, min_w, depth)


def part_2():
    cave, max_w, min_w, depth = parse_file()
    depth += 2
    max_w = max_w + depth
    min_w = min_w - depth
    create_floor(cave, max_w, min_w, depth)

    find_air(cave, max_w, min_w, depth)
    return simulate_falling_send(cave, max_w, min_w, depth)


print("Part 1:", part_1())
print("Part 2:", part_2())
