import re


def format_stacks(file):
    all_stacks = []
    for line in file:
        find_end_of_stacks = list(line)
        all_stacks.append(find_end_of_stacks)
        stack_num_list = []
        for stack_num, num in enumerate(find_end_of_stacks):
            if num.isnumeric():
                stack_num_list.append(stack_num)
        if stack_num_list:
            all_stacks.pop()
            return stack_num_list, len(stack_num_list), all_stacks


def _get_stacks(stack_num_list, num_of_stacks, all_stacks):
    stacks = {}
    for i in range(num_of_stacks):
        stacks[f"stack_{i+1}"] = []
        for stack in all_stacks:
            if stack[stack_num_list[i]] != " ":
                stacks[f"stack_{i+1}"].append(stack[stack_num_list[i]])
    return stacks


def get_stacks(file):
    stack_num_list, num_of_stacks, all_stacks = format_stacks(file)
    return _get_stacks(stack_num_list, num_of_stacks, all_stacks)


def move_one_from_to_stack(stacks, move_from, move_to, ammount):
    for i in range(ammount):
        x = stacks[f"stack_{move_from}"].pop(0)
        stacks[f"stack_{move_to}"].insert(0, x)


def move_multiple_from_to_stack(stacks, move_from, move_to, ammount):
    x: list = stacks[f"stack_{move_from}"][0:ammount]
    del stacks[f"stack_{move_from}"][0:ammount]
    x.reverse()
    for y in x:
        stacks[f"stack_{move_to}"].insert(0, y)


def creates_on_top(stacks):
    result = ""
    for k, v in stacks.items():
        result += v[0]
    return result


def part_1():
    with open("input.txt", "r") as file:
        stacks = get_stacks(file)
        for line in file:
            x = re.findall(r'\d+', line.strip())
            if not x:
                continue
            move_one_from_to_stack(stacks, x[1], x[2], int(x[0]))
        return creates_on_top(stacks)


def part_2():
    with open("input.txt", "r") as file:
        stacks = get_stacks(file)
        for line in file:
            x = re.findall(r'\d+', line.strip())
            if not x:
                continue
            move_multiple_from_to_stack(stacks, x[1], x[2], int(x[0]))
        return creates_on_top(stacks)


print("Part 1:", part_1())
print("Part 2:", part_2())
