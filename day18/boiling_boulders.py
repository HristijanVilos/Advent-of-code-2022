from collections import deque


def have_adjacent_side(cube_1, cube_2) -> bool:
    if cube_1[0] + 1 == cube_2[0] or cube_1[0] == cube_2[0] + 1:
        if cube_1[1] == cube_2[1] and cube_1[2] == cube_2[2]:
            return True
    if cube_1[1] + 1 == cube_2[1] or cube_1[1] == cube_2[1] + 1:
        if cube_1[0] == cube_2[0] and cube_1[2] == cube_2[2]:
            return True
    if cube_1[2] + 1 == cube_2[2] or cube_1[2] == cube_2[2] + 1:
        if cube_1[0] == cube_2[0] and cube_1[1] == cube_2[1]:
            return True
    return False


def starting_position(cubes):
    min_x = min([x[0] for x in cubes])
    min_y = min([x[1] for x in cubes])
    min_z = min([x[2] for x in cubes])
    return min_x-1, min_y-1, min_z-1


def ending_position(cubes):
    max_x = max([x[0] for x in cubes])
    max_y = max([x[1] for x in cubes])
    max_z = max([x[2] for x in cubes])
    return max_x+1, max_y+1, max_z+1


def create_grid(start_pos: tuple, end_pos: tuple):
    min_x, min_y, min_z = start_pos[0], start_pos[1], start_pos[2]
    max_x, max_y, max_z = end_pos[0], end_pos[1], end_pos[2]
    grid = []
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            for z in range(min_z, max_z):
                grid.append((x, y, z))
    return grid


def valid_nodes(node: tuple, start_pos: tuple,
                end_pos: tuple, lava_droplets: dict):
    posible_moves = [(1, 0, 0), (-1, 0, 0),
                     (0, 1, 0), (0, -1, 0),
                     (0, 0, 1), (0, 0, -1)]
    available_nodes = []
    for move in posible_moves:
        x, y, z = node[0] + move[0], node[1] + move[1], node[2] + move[2]
        if (x >= start_pos[0] and y >= start_pos[1] and z >= start_pos[2])\
                and (x <= end_pos[0] and y <= end_pos[1] and z <= end_pos[2])\
                and (x, y, z) not in lava_droplets:
            available_nodes.append((x, y, z))
    return available_nodes


def calculate_total_sides(number_of_cubes: int):
    return 6*number_of_cubes


def parse():
    with open("input.txt", "r") as file:
        return [(int(line.strip().split(",")[0]),
                 int(line.strip().split(",")[1]),
                 int(line.strip().split(",")[2]))
                for line in file]


def part_1(cubes: list[tuple]):
    count = 0
    num_of_cubes = len(cubes)
    for i in range(num_of_cubes):
        for j in range(i+1, num_of_cubes):
            if have_adjacent_side(cubes[i], cubes[j]):
                count += 1

    total_sides = calculate_total_sides(num_of_cubes)

    return (total_sides - 2*count)


def part_2(cubes: list[tuple]):
    start_pos = starting_position(cubes)
    end_pos = ending_position(cubes)
    grid = create_grid(start_pos, end_pos)
    lava_droplets = {cube: True for cube in cubes}
    outside = {}
    queue = deque()
    queue.append(start_pos)
    while queue:
        node = queue.popleft()
        if outside.get(node):
            continue
        outside[node] = True
        for _node in valid_nodes(node, start_pos, end_pos, lava_droplets):
            queue.append(_node)
    inside_nodes = []
    for node in grid:
        if node in outside or node in lava_droplets:
            continue
        inside_nodes.append(node)

    total_sides = part_1(cubes)
    inside_total_sides = part_1(inside_nodes)

    return total_sides-inside_total_sides


cubes = parse()
print("Part 1:", part_1(cubes))
print("Part 2:", part_2(cubes))
