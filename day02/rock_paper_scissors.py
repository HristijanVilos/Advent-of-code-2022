switcher = {
        "AX": 4,
        "BX": 1,
        "CX": 7,
        "AY": 8,
        "BY": 5,
        "CY": 2,
        "AZ": 3,
        "BZ": 9,
        "CZ": 6
    }

with open("input.txt", "r") as file:
    result_1 = 0
    result_2 = 0
    for line in file:
        rpc = "".join(line.strip().split(" "))
        result_1 += switcher.get(rpc)
        outcome = [v for k, v in switcher.items() if k.startswith(rpc[0])]
        outcome.sort()
        if rpc[1] == "X":
            result_2 += outcome[0]
        elif rpc[1] == "Y":
            result_2 += outcome[1]
        elif rpc[1] == "Z":
            result_2 += outcome[2]


def part_1():
    return result_1


def part_2():
    return result_2


print("Part 1: ", part_1())
print("Part 2: ", part_2())
