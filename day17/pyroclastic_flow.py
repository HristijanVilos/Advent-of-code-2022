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


def starting_pos(pos: int, shape: tuple) -> list:
    res = []
    for s in shape:
        res.append([s[0] + pos, s[1] + 2])
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


def signature(maxX, grid):
    # maxX-x<= save the last number of rows
    # 4 is the lowest number of last rows of signiture that can prove
    # the pattern for my case (found iteratively)
    return frozenset([(maxX - x, y) for (x, y) in grid if maxX - x <= 4])


def update_grid(grid: set, dh: int, times_repeating: int):
    new_grid = set()
    for (x, y) in grid:
        new_grid.add((x+(dh*times_repeating), y))
    return new_grid


def solution(H: int):
    grid = set([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])
    directions = parse()
    len_dir = len(directions)
    count = 0
    move = 0
    max_height = 0
    paterns_seen = {}
    once = True
    while move < H:
        shape = SHAPES[move % 5]
        can_proceed = True
        pos = max_height + 4
        cur_pos = starting_pos(pos, shape)
        while can_proceed:
            dir_num = count % len_dir
            _dir = directions[dir_num]
            count += 1
            DIR.get(_dir)(cur_pos, grid)
            if can_move_down(cur_pos, grid):
                move_down(cur_pos)
            else:
                max_height = setled_rock(cur_pos, grid, max_height)
                # the place in the direction pattern, the shape,
                # signature of the last rows (in my case 4 is enough 🤯)
                SR = (dir_num, move % 5, signature(max_height, grid))
                can_proceed = False

                if SR in paterns_seen and once:
                    once = False
                    (old_move, old_height) = paterns_seen[SR]
                    dm = move - old_move
                    dh = max_height - old_height
                    times_repeating = (H - move) // dm
                    max_height += times_repeating * dh
                    move += times_repeating * dm
                    grid = update_grid(grid, dh, times_repeating)
                    break
                paterns_seen[SR] = (move, max_height)
        move += 1
    return max_height


print("Part 1:", solution(H=2022))
print("Part 2:", solution(H=1_000_000_000_000))
