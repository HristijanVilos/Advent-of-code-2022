import re


FACING = ((0, 1), (1, 0), (0, -1), (-1, 0))


def parse_key(monkey_key):
    _stkey = ""
    lmk = []
    for x in monkey_key:
        if x.isalpha():
            y = re.split("(\d+)", _stkey)
            lmk.append((y[0], int(y[1])))
            _stkey = ""
        _stkey += x
    y = re.split("(\d+)", _stkey)
    lmk.append((y[0], int(y[1])))
    return lmk


def can_move(cur_pos, monkey_map_dict: dict):
    if cur_pos[1] == 0:
        x = min(k for k in monkey_map_dict.keys() if k[0] == cur_pos[0][0])
        return x, monkey_map_dict[x]
    elif cur_pos[1] == 2:
        x = max(k for k in monkey_map_dict.keys() if k[0] == cur_pos[0][0])
        return x, monkey_map_dict[x]
    elif cur_pos[1] == 1:
        x = min(k for k in monkey_map_dict.keys() if k[1] == cur_pos[0][1])
        return x, monkey_map_dict[x]
    elif cur_pos[1] == 3:
        x = max(k for k in monkey_map_dict.keys() if k[1] == cur_pos[0][1])
        return x, monkey_map_dict[x]


def part_1():
    monkey_map_dict = {}
    with open("input.txt", "r") as file:
        map_key = file.read().split("\n\n")
        monkey_map = map_key[0]
        monkey_key = map_key[1]
        for i, line in enumerate(monkey_map.splitlines()):
            for j, char in enumerate(line):
                if char == " ":
                    continue
                elif char == ".":
                    monkey_map_dict[(i+1, j+1)] = True
                else:
                    monkey_map_dict[(i+1, j+1)] = False

        lmk = parse_key(monkey_key)
        start_pos = min(k for k, v in monkey_map_dict.items()
                        if k[0] == 1 and v is True)
        cur_pos = [(start_pos[0], start_pos[1]), 0]

        for move in lmk:
            if move[0] == "R":
                cur_pos[1] = (cur_pos[1] + 1) % 4
            elif move[0] == "L":
                cur_pos[1] = (cur_pos[1] - 1) % 4
            for _ in range(move[1]):
                x = (cur_pos[0][0] + FACING[cur_pos[1]][0],
                     cur_pos[0][1] + FACING[cur_pos[1]][1])
                test_case = monkey_map_dict.get(x)
                if test_case:
                    cur_pos[0] = x
                elif test_case is False:
                    break
                elif test_case is None:
                    x, test = can_move(cur_pos, monkey_map_dict)
                    if test:
                        cur_pos[0] = x
                    else:
                        break
        return cur_pos[0][0]*1000 + cur_pos[0][1]*4 + cur_pos[1]


def part_2():
    pass


print("Part 1:", part_1())
print("Part 2:", part_2())
