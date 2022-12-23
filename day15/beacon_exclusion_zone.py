import re


def parse_file():
    sensors = {}
    beacons = {}
    with open("input.txt", "r") as file:
        for line in file:
            y, x, z, w = [int(_) for _ in re.findall(r'-?\d+', line.strip())]
            d = abs(y-z) + abs(x-w)
            sensors[(y, x)] = d
            beacons[(z, w)] = True
    return sensors, beacons


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


def create_outer_perimetar(sensor, d, perimetar_set: set, MIN_X, MAX_X):
    min_x, max_x = sensor[0] - d, sensor[0] + d
    min_y, max_y = sensor[1] - d, sensor[1] + d
    test = False
    y1, y2 = sensor[1], sensor[1]
    if y1 >= MIN_X and y1 <= MAX_X:
        if min_x > MIN_X:
            perimetar_set.add((y1, min_x))
        if max_x < MAX_X:
            perimetar_set.add((y1, max_x))
    for x in range(min_x+1, max_x+1):
        if not test:
            y1 = y1 + 1
            y2 = y2 - 1
            if y1 == max_y and y2 == min_y:
                test = True
        else:
            y1 = y1 - 1
            y2 = y2 + 1
        if x < MIN_X or x > MAX_X:
            continue
        else:
            if y1 > MIN_X or y1 < MAX_X:
                perimetar_set.add((y1, x))
            if y2 > MIN_X or y2 < MAX_X:
                perimetar_set.add((y2, x))


def can_sensor_reach(sensor, d, p):
    return d >= abs(sensor[1] - p[1]) + abs(sensor[0] - p[0])


def part_1():
    row_y = 2000000
    sensors, beacons = parse_file()
    result_set = set()
    for sensor, d in sensors.items():
        if can_reach(sensor, d, row_y):
            create_points(sensor, d, row_y, beacons, result_set)
    return len(result_set)


def part_2():
    MIN_X, MAX_X = 0, 4000000
    sensors, beacons = parse_file()
    perimetar_set = set()
    for sensor, d in sensors.items():
        create_outer_perimetar(sensor, d+1, perimetar_set, MIN_X, MAX_X)

    perimetar_list = list(perimetar_set)

    for x in perimetar_list:
        test = False
        if x[0] < MIN_X or x[1] < MIN_X or x[0] > MAX_X or x[1] > MAX_X:
            continue
        for sensor, d in sensors.items():
            test = test or can_sensor_reach(sensor, d, x)
            if test:
                break
        if not test:
            return x[0]*4000000 + x[1]


print("Part 1:", part_1())
print("Part 2:", part_2())
