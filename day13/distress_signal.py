import itertools
import functools


def is_in_right_order(first, second):
    for f, s in itertools.zip_longest(first, second):
        if type(f) == type(s) and isinstance(f, int):
            if f > s:
                return False
            elif f < s:
                return True
            else:
                continue
        if type(f) == type(s) and isinstance(f, list):
            x = is_in_right_order(f, s)
            if x is None:
                continue
            elif x:
                return True
            else:
                return False
        if type(f) != type(s):
            if isinstance(f, int) and isinstance(s, list):
                f_l = [f]
                x = is_in_right_order(f_l, s)
                if x is None:
                    continue
                elif x:
                    return True
                else:
                    return False
            elif isinstance(f, list) and isinstance(s, int):
                s_l = [s]
                x = is_in_right_order(f, s_l)
                if x is None:
                    continue
                elif x:
                    return True
                else:
                    return False
            elif (isinstance(f, int) or isinstance(f, list)) and s is None:
                return False
            elif (isinstance(s, int) or isinstance(s, list)) and f is None:
                return True
    return None


def _compare(first, second):
    x = is_in_right_order(first, second)
    if x is None:
        return 0
    elif x:
        return -1
    else:
        return 1


def part_1():
    with open("input.txt", "r") as file:
        pairs = []
        pair = []
        for line in file.read().splitlines():
            if line == "":
                pairs.append(pair)
                pair = []
                continue
            pair.append(eval(line))
        pairs.append(pair)
        result = 0
        for i, pair in enumerate(pairs):
            x = is_in_right_order(pair[0], pair[1])
            if x:
                result += i+1
        return result


def part_2():
    with open("input.txt", "r") as file:
        lines = []
        for line in file.read().splitlines():
            if line == "":
                continue
            lines.append(eval(line))
        lines.append([[2]])
        lines.append([[6]])
        lines.sort(key=functools.cmp_to_key(_compare))
        result = 1
        for i, li in enumerate(lines):
            if li == [[2]]:
                result *= (i+1)
            elif li == [[6]]:
                result *= (i+1)
    return result


print("Part 1:", part_1())
print("Part 2:", part_2())
