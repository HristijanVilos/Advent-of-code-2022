switcher={
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


def part_1():
    with open("input.txt", "r") as file:
        result = 0
        for line in file:
            str1 = ""
            rpc_list = line.strip().split(" ")
            rpc = str1.join(rpc_list)
            result += switcher.get(rpc)
        
        return result


def part_2():
    with open("input.txt", "r") as file:
        result = 0
        for line in file:
            str1 = ""
            rpc_list = line.strip().split(" ")
            rpc = str1.join(rpc_list)
            outcome = [v for k, v in switcher.items() if k.startswith(rpc[0])]
            outcome.sort()
            if rpc[1] == "X":
                result += outcome[0]
            elif rpc[1] == "Y":
                result += outcome[1]
            elif rpc[1] == "Z":
                result += outcome[2]
        
        return result 

print("Part 1: ", part_1())
print("Part 2: ", part_2())

