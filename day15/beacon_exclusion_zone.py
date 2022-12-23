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


def create_perimtar(sensor, d, perimetar_set: set, MAX_X):
    min_x, max_x = sensor[0] - d, sensor[0] + d
    min_y, max_y = sensor[1] - d, sensor[1] + d
    test = False
    x1, x2 = sensor[0], sensor[0]
    for i, y in enumerate(range(min_y, max_y)):
        if not test:
            x1 = x1 + 1
            x2 = x2 - 1
            if x1 == min_x and x2 == max_x:
                test = True
        else:
            x1 = x1 - 1
            x2 = x2 + 1
        if y < 0 or y > MAX_X:
            continue
        else:
            if x1 > 0 or x1 < MAX_X:
                perimetar_set.add((x1, y))
            if x2 > 0 or x2 < MAX_X:
                perimetar_set.add((x2, y))


def can_sensor_reach(sensor, d, p):
    return d >= abs(sensor[1] - p[1]) + abs(sensor[0] - p[0])


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
    MAX_X = 4000000
    sensors = {}
    beacons = {}
    with open("input.txt", "r") as file:
        for line in file:
            y, x, z, w = [int(_) for _ in re.findall(r'-?\d+', line.strip())]
            d = abs(y-z) + abs(x-w)
            sensors[(y, x)] = d
            beacons[(z, w)] = True

        perimetar_set = set()
        for sensor, d in sensors.items():
            print(sensor)
            create_perimtar(sensor, d, perimetar_set, MAX_X)

        for r in perimetar_set:
            points = [(1, 0), (1, 1), (0, 1), (-1, 1),
                      (-1, 0), (-1, -1), (0, -1), (1, -1)]
            new_points = []
            for p in points:
                new_points.append((r[0]+p[0], r[1]+p[1]))
            for x in new_points:
                test = False
                if x[0] < 0 or x[1] < 0 or x[0] > MAX_X or x[1] > MAX_X:
                    continue
                for sensor, d in sensors.items():
                    test = test or can_sensor_reach(sensor, d, x)
                    if test:
                        break

                if not test:
                    return x[0]*4000000 + x[1]


print("Part 1:", part_1())
print("Part 2:", part_2())
