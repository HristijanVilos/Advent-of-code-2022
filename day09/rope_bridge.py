DIR = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 0),
    "D": (-1, 0)
}


def move_head(pos_h, dir):
    return [pos_h[0]+dir[0], pos_h[1]+dir[1]]


def move_tail(pos_h, pos_t, dir):
    if abs(pos_h[0] - pos_t[0]) <= 1 and abs(pos_h[1] - pos_t[1]) <= 1:
        return pos_t
    else:
        return [pos_h[0]-dir[0], pos_h[1]-dir[1]]


def follow(loc_h, loc_t):
    if abs(loc_h[0] - loc_t[0]) <= 1 and abs(loc_h[1] - loc_t[1]) <= 1:
        return loc_t
    if (loc_h[0] - loc_t[0]) > 1:
        _check_j_direction(loc_h, loc_t)
        loc_t[0] += 1
    elif (loc_t[0] - loc_h[0]) > 1:
        _check_j_direction(loc_h, loc_t)
        loc_t[0] -= 1
    elif (loc_h[1] - loc_t[1]) > 1:
        _check_i_direction(loc_h, loc_t)
        loc_t[1] += 1
    elif (loc_t[1] - loc_h[1]) > 1:
        _check_i_direction(loc_h, loc_t)
        loc_t[1] -= 1
    return loc_t


def _check_j_direction(loc_h, loc_t):
    if (loc_h[1] - loc_t[1]) > 0:
        loc_t[1] += 1
    elif (loc_t[1] - loc_h[1]) > 0:
        loc_t[1] -= 1


def _check_i_direction(loc_h, loc_t):
    if (loc_h[0] - loc_t[0]) > 0:
        loc_t[0] += 1
    elif (loc_t[0] - loc_h[0]) > 0:
        loc_t[0] -= 1


def part_1():
    with open("input.txt", "r") as file:
        pos_h = [0, 0]
        pos_t = [0, 0]
        result = {}
        for line in file:
            dir = DIR[line.strip().split()[0]]
            move = int(line.strip().split()[1])
            for step in range(move):
                pos_h = move_head(pos_h, dir)
                pos_t = follow(pos_h, pos_t)
                result[f"{pos_t}"] = True

    return len(result)


def part_2():
    with open("input.txt", "r") as file:
        pos_h = [0, 0]
        pos_t = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
                 [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        result = {}
        for line in file:
            dir = DIR[line.strip().split()[0]]
            move = int(line.strip().split()[1])
            for step in range(move):
                pos_h = move_head(pos_h, dir)
                pos_t[0] = pos_h
                for i in range(0, 9):
                    follow(pos_t[i], pos_t[i+1])
                last_knot = pos_t[9]
                result[f"{last_knot}"] = True

    return len(result)


print("Part 1:", part_1())
print("Part 2:", part_2())
