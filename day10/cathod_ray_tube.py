def go_through_cycle(X, cycle, program_cycle: list,
                     instruction, num_add, screen):
    if instruction == "noop":
        draw_pixel(cycle, X, screen)
        cycle += 1
        program_cycle.append([cycle, X])
    else:
        draw_pixel(cycle, X, screen)
        cycle += 1
        program_cycle.append([cycle, X])
        draw_pixel(cycle, X, screen)
        cycle += 1
        program_cycle.append([cycle, X])
        X += num_add
    return X, cycle


def signal_strength(program_cycle, num: int):
    return program_cycle[num][0] * program_cycle[num][1]


def sum_signal_strengths(program_cycle, *nums):
    result = 0
    for num in nums:
        result += signal_strength(program_cycle, num)
    return result


def draw_screen():
    screen = []
    for i in range(6):
        row = []
        for j in range(40):
            row.append(".")
        screen.append(row)
    return screen


def draw_pixel(cycle, X, screen: list[list[str]]):
    height = int(cycle/40)
    position = cycle % 40
    if (X-1) == position or X == position or (X+1) == position:
        screen[height][position] = "#"


def join_and_print(screen):
    for row in screen:
        x = "".join(row)
        print(x)


def part_1():
    with open("input.txt", "r") as file:
        X = 1
        cycle = 0
        program_cycle = [[cycle, X]]
        screen = draw_screen()
        for line in file:
            instruction = line.strip().split(" ")[0]
            if instruction == "addx":
                num_add = int(line.strip().split(" ")[1])
            else:
                num_add = 0

            X, cycle = go_through_cycle(X, cycle, program_cycle,
                                        instruction, num_add, screen)
        print("Part 2:")
        join_and_print(screen)
        return sum_signal_strengths(program_cycle, 20, 60, 100, 140, 180, 220)


print("Part 1:", part_1())
