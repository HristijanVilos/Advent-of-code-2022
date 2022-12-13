with open("input.txt", "r") as file:
    calories = 0
    result = []
    for line in file:
        line = line.strip()
        if line:
            calories += int(line)
        else:
            result.append(calories)
            calories = 0
    result.sort(reverse=True)


def part_1():
    return result[0]


def part_2():
    return result[0] + result[1] + result[2]


print("Part 1: ", part_1())
print("Part 2: ", part_2())
