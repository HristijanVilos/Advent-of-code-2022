def parse():
    result = {}
    with open("input.txt", "r") as file:
        for line in file:
            x = line.strip().split(":")
            result[x[0]] = int(x[1].strip())\
                if x[1].strip().isnumeric() else x[1].strip()
    return result


def part_1():
    result = parse()
    return int(find_result_for_monkey(result, "root"))


def part_2():
    result = parse()
    return solve(result)


def find_result_for_monkey(result, name):
    if isinstance(result[name], int):
        return result[name]
    else:
        x = find_result_for_monkey(result, result[name].split()[0])
        y = find_result_for_monkey(result, result[name].split()[2])
        return eval(result[name], {},
                    {result[name].split()[0]: x, result[name].split()[2]: y})


def solve(result: dict):
    # x = y => x - y = 0 => x.real - y.real + x.img - y.img = 0
    # x.r - y.r = -(x.i - y.i) in this case the imag "i" part will
    # give us the solution i.e. i = x.r -y.r/(-(x.i-y.i))
    x = find_result_for_humn(result, result["root"].split()[0])
    y = find_result_for_humn(result, result["root"].split()[2])
    real = x.real - y.real
    imag = -(x.imag - y.imag)
    return int(real/imag)


def find_result_for_humn(result, name):
    if name == "humn":
        return 1j
    if isinstance(result[name], int):
        return result[name]
    else:
        x = find_result_for_humn(result, result[name].split()[0])
        y = find_result_for_humn(result, result[name].split()[2])
        return eval(result[name], {},
                    {result[name].split()[0]: x, result[name].split()[2]: y})


print("Part 1:", part_1())
print("Part 2:", part_2())
