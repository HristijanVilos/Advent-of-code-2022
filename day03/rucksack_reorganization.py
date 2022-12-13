def get_compartments(rucksack):
    items_per_compartment = int(len(rucksack)/2)
    compartment_1 = rucksack[0:items_per_compartment]
    compartment_2 = rucksack[items_per_compartment: len(rucksack)]
    return compartment_1, compartment_2


def find_same_chars(compartment_1, compartment_2):
    same_chars = []
    for char in set(compartment_1):
        for char_2 in set(compartment_2):
            if char == char_2:
                same_chars.append(char_2)
    return same_chars


def value_of_char(chars):
    result = 0
    for char in chars:
        if char.islower():
            result += ord(char) - 96
        else:
            result += ord(char) - 38
    return result


def part_1():
    with open("input.txt", "r") as file:
        result = 0
        for line in file:
            rucksack = line.strip()
            compartment_1, compartment_2 = get_compartments(rucksack)
            same_chars = find_same_chars(compartment_1, compartment_2)
            result += value_of_char(same_chars)

    return result


def part_2():
    with open("input.txt", "r") as file:
        result = 0
        while True:
            line_1 = file.readline().strip()
            line_2 = file.readline().strip()
            line_3 = file.readline().strip()
            if not line_1:
                break
            same_chars_12 = find_same_chars(line_1, line_2)
            same_chars_123 = find_same_chars(same_chars_12, line_3)
            result += value_of_char(same_chars_123)

    return result


print("Part 1: ", part_1())
print("Part 2: ", part_2())
