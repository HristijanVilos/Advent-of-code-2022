def part_1():
    with open("input.txt", "r") as file:
        max_calories = 0
        calories = 0
        for line in file:
            if line not in ['\n', '\r\n']:
                calories += int(line)
            if line.strip() == "":
                if calories > max_calories:
                    max_calories = calories
                calories = 0

    return max_calories


def part_2():
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
        if calories:
            result.append(calories)


        result.sort(reverse=True)

    return result[0] + result[1] + result[2]


print("Part 1: ", part_1())
print("Part 2: ", part_2())
