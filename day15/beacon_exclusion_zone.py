import re


def can_reach(sensor: tuple, d, row_y):
    return d > abs(sensor[1] - row_y)


# |x1 - x2| + |y1 - y2| = d
# |s[0] - x| + |s[1] - row_y| = d
# |s[0] - x| = d - |s[1] - row_y|
# x = +-(d - |s[1] - row_y|) + s[0]
# from -(d - |s[1] - row_y|) + s[0] to + (d - |s[1] - row_y|) + s[0]
def create_points(s: tuple, d, row_y, beacons, result_set):
    _min_x = -(d - abs(s[1]-row_y)) + s[0]
    _max_x = (d - abs(s[1]-row_y)) + s[0]
    max_x, min_x = max(_min_x, _max_x), min(_min_x, _max_x)
    for i in range(min_x, max_x+1, 1):
        if not beacons.get((i, row_y), False):
            result_set.add((i, row_y))


def part_1():
    row_y = 2000000
    sensors = {}
    beacons = {}
    with open("input.txt", "r") as file:
        for line in file:
            y, x, z, w = [int(_) for _ in re.findall(r'-?\d+', line.strip())]
            d = abs(y-z) + abs(x-w)
            sensors[(y, x)] = d
            beacons[(z, w)] = True
        result_set = set()
        for sensor, d in sensors.items():
            if can_reach(sensor, d, row_y):
                create_points(sensor, d, row_y, beacons, result_set)
        return len(result_set)


def part_2():
    min_x, max_x = 0, 20
    min_y, max_y = 0, 20
    sensors = {}
    beacons = {}
    with open("test_input.txt", "r") as file:
        for line in file:
            y, x, z, w = [int(_) for _ in re.findall(r'-?\d+', line.strip())]
            d = abs(y-z) + abs(x-w)
            sensors[(y, x)] = d
            beacons[(z, w)] = True
        result_set = set()



print("Part 1:", part_1())
print("Part 2:", part_2())
