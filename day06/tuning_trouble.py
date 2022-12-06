def start_of_packet(file):
    sub_str = ""
    count = 0
    for i, char in enumerate(file.readline()):
        if char not in sub_str:
            sub_str += char
            count += 1
        else:
            sub_str = sub_str.split(char)[1]
            sub_str += char
            count = len(sub_str)
        if count == 4:
            return (i+1)


def start_of_message(file):
    sub_str = ""
    count = 0
    for i, char in enumerate(file.readline()):
        if char not in sub_str:
            sub_str += char
            count += 1
        else:
            sub_str = sub_str.split(char)[1]
            sub_str += char
            count = len(sub_str)
        if count == 14:
            return (i + 1)


def part_1():
    with open("input.txt", "r") as file:
        return start_of_packet(file)


def part_2():
    with open("input.txt", "r") as file:
        return start_of_message(file)


print("Part 1:", part_1())
print("Part 2:", part_2())
