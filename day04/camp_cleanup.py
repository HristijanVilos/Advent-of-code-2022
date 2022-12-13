def get_two_elfs(line):
    return line.strip().split(",")


def sections_ID_for_elf(elf: str):
    start, end = elf.split("-")
    start = int(start)
    end = int(end) + 1
    result_str = ""
    for i in range(start, end, 1):
        if i < 10:
            # so it would make 1-2 diffrent form 12-whatever
            # if not this 1-2 will be found as a substring of 12-whatever
            result_str += "-"
        result_str += str(i)
        result_str += "+"
    return result_str


def sections_ID_for_elf_list(elf: str):
    start, end = elf.split("-")
    start = int(start)
    end = int(end) + 1
    result_list = []
    for i in range(start, end, 1):
        result_list.append(i)
    return result_list


def are_sections_overlaping(first_elf_clean, second_elf_clean):
    for i in first_elf_clean:
        for j in second_elf_clean:
            if i == j:
                return True
    return False


def part_1():
    with open("input.txt", "r") as file:
        result = 0
        for line in file:
            first_elf, second_elf = get_two_elfs(line)
            first_elf_clean = sections_ID_for_elf_list(first_elf)
            second_elf_clean = sections_ID_for_elf_list(second_elf)
            if (first_elf_clean in second_elf_clean)\
                    or (second_elf_clean in first_elf_clean):
                result += 1

    return result


def part_2():
    with open("input.txt", "r") as file:
        result = 0
        for line in file:
            first_elf, second_elf = get_two_elfs(line)
            first_elf_clean = sections_ID_for_elf_list(first_elf)
            second_elf_clean = sections_ID_for_elf_list(second_elf)
            if are_sections_overlaping(first_elf_clean, second_elf_clean):
                result += 1

        return result


print("Part 1:", part_1())
print("Part 2:", part_2())
