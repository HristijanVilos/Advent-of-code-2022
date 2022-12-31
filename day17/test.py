SHAPES = (
    # minus
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    # plus
    ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
    # L shape
    ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2)),
    # I
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    # Block
    ((0, 0), (0, 1), (1, 0), (1, 1))
    )


def move_right(cur_pos: list, grid: set):
    if can_move_right(cur_pos, grid):
        for s in cur_pos:
            s[1] += 1


def move_left(cur_pos: list, grid: set):
    if can_move_left(cur_pos, grid):
        for s in cur_pos:
            s[1] -= 1


def move_down(cur_pos: list):
    for s in cur_pos:
        s[0] -= 1


def can_move_right(cur_pos: list, grid: set):
    for i in cur_pos:
        if i[1]+1 > 6 or (i[0], i[1] + 1) in grid:
            return False
    return True


def can_move_left(cur_pos: list, grid: set):
    for i in cur_pos:
        if i[1]-1 < 0 or (i[0], i[1] - 1) in grid:
            return False
    return True


def can_move_down(cur_pos: list, grid: set):
    for c in cur_pos:
        if (c[0] - 1, c[1]) in grid:
            return False
    return True


def calc_cur_pos(pos: int, shape: tuple) -> list:
    res = []
    for s in shape:
        res.append([s[0] + pos, s[1] +2])
    return res


def setled_rock(cur_pos: list, grid: set, max_height: int):
    for c in cur_pos:
        if c[0] > max_height:
            max_height = c[0]
        grid.add(tuple(c))
    return max_height


DIR = {
    ">": move_right,
    "<": move_left,
}


def parse() -> str:
    with open("input.txt", "r") as file:
        return file.read()


def part_1():
    grid = set([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])
    directions = parse()
    len_dir = len(directions)
    count = 0
    max_height = 0
    for move in range(2022):
        shape = SHAPES[move%5]
        can_proceed = True
        pos = max_height + 4
        cur_pos = calc_cur_pos(pos, shape)
        while can_proceed:
            get_dir = count % len_dir
            _dir = directions[get_dir]
            count += 1
            DIR.get(_dir)(cur_pos, grid)
            if can_move_down(cur_pos, grid):
                move_down(cur_pos)
            else:
                max_height = setled_rock(cur_pos, grid, max_height)
                can_proceed = False

    return max_height


def part_2():
    grid = set([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])
    directions = parse()
    len_dir = len(directions)
    count = 0
    max_height = 0
    for move in range(1_000_000_000_000):
        shape = SHAPES[move%5]
        can_proceed = True
        pos = max_height + 4
        cur_pos = calc_cur_pos(pos, shape)
        
        while can_proceed:
            get_dir = count % len_dir
            _dir = directions[get_dir]
            count += 1
            DIR.get(_dir)(cur_pos, grid)
            if can_move_down(cur_pos, grid):
                move_down(cur_pos)
            else:
                max_height = setled_rock(cur_pos, grid, max_height)
                can_proceed = False

    return max_height


print("Part 1:", part_1())
# print("Part 2:", part_2())
