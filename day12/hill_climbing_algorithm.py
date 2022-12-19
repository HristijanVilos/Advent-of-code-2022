def valid_moves(i, j, l_p, grid):
    posible_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    available_moves = []
    for move in posible_moves:
        x = i + move[0]
        y = j + move[1]
        if (x >= 0 and y >= 0) and (x <= l_p[0] and y <= l_p[1])\
                and (grid[(x, y)] - grid[(i, j)] <= 1):
            available_moves.append((x, y))
    return available_moves


def parse_file():
    with open("input.txt", "r") as file:
        grid = {}
        for i, row in enumerate(file.read().splitlines()):
            for j, char in enumerate(row):
                if char == "S":
                    starting_position = (i, j)
                    grid[i, j] = 0
                elif char == "E":
                    ending_position = (i, j)
                    grid[i, j] = 27
                else:
                    grid[i, j] = ord(char)-96
        last_position = (i, j)
    return grid, starting_position, ending_position, last_position


def find_distances(grid, last_position, result, queue):
    while len(queue) != 0:
        dist, node = queue.pop(0)

        if result.get(node):
            continue
        result[node] = dist

        for move in valid_moves(node[0], node[1], last_position, grid):
            queue.append((dist+1, move))


def part_1():
    grid, starting_position, ending_position, last_position = parse_file()
    result = {}
    queue = []
    queue.append((0, starting_position))
    find_distances(grid, last_position, result, queue)

    return result[ending_position]


def part_2():
    grid, starting_position, ending_position, last_position = parse_file()
    grid[starting_position] = 1
    result = {}
    queue = []
    for start, value in grid.items():
        if value == 1:
            queue.append((0, start))
    find_distances(grid, last_position, result, queue)

    return result[ending_position]


print("Part 1:", part_1())
print("Part 2:", part_2())
