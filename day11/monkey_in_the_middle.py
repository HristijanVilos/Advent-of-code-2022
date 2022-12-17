def parse():
    with open("input.txt", "r") as file:
        monkeys = {}
        monkeys_list = file.read().split("\n\n")
        for count, monkey in enumerate(monkeys_list):
            x = []
            [x.append(y.strip()) for y in monkey.strip().split('\n')]
            starting_items = x[1].strip().split(":")[1]
            starting_items = [int(item) for item in starting_items.strip().split(",")]
            operation = x[2].split("=")[1].strip()
            monkeys[f"monkey_{count}"] = {
                "starting_items": starting_items,
                "operation": operation,
                "divisible": int(x[3].split()[-1]),
                "if_true": int(x[4].split()[-1]),
                "if_false": int(x[5].split()[-1]),
                "inspected": 0
            }
        product = 1
        for x in monkeys.values():
            product *= x["divisible"]
    return monkeys, product


def _operation(worry_lvl, operation):
    return eval(operation, {}, {"old": worry_lvl})


def _divisible(monkeys: dict, monkey: dict, worry_lvl: int):
    divisor = monkey["divisible"]
    modulo = worry_lvl % divisor
    if modulo == 0:
        x = monkey["if_true"]
        monkeys[f"monkey_{x}"]["starting_items"].append(worry_lvl)
    else:
        x = monkey["if_false"]
        monkeys[f"monkey_{x}"]["starting_items"].append(worry_lvl)


def _divisible_2(monkeys: dict, monkey: dict, worry_lvl: int, product: int):
    divisor = monkey["divisible"]
    worry_lvl = worry_lvl % product
    modulo = worry_lvl % divisor
    if modulo == 0:
        x = monkey["if_true"]
        monkeys[f"monkey_{x}"]["starting_items"].append(worry_lvl)
    else:
        x = monkey["if_false"]
        monkeys[f"monkey_{x}"]["starting_items"].append(worry_lvl)


def round(monkeys: dict, product: int):
    for monkey in monkeys.values():
        for item_worry_level in monkey["starting_items"]:
            item_worry_level = _operation(item_worry_level, monkey["operation"])
            item_worry_level //= 3
            _divisible(monkeys, monkey, item_worry_level)
        monkey["inspected"] += len(monkey["starting_items"])
        monkey["starting_items"] = []


def round_2(monkeys: dict, product: int):
    for monkey in monkeys.values():
        for item_worry_level in monkey["starting_items"]:
            item_worry_level = _operation(item_worry_level, monkey["operation"])
            _divisible_2(monkeys, monkey, item_worry_level, product)
        monkey["inspected"] += len(monkey["starting_items"])
        monkey["starting_items"] = []


def monkey_business(monkeys: dict):
    monkey_business = []
    for monkey in monkeys.values():
        monkey_business.append(monkey["inspected"])
    monkey_business.sort()
    return monkey_business[-1] * monkey_business[-2]


def part_1():
    monkeys, product = parse()
    for i in range(20):
        round(monkeys, product)
    return monkey_business(monkeys)


def part_2():
    monkeys, product = parse()
    for i in range(10_000):
        round_2(monkeys, product)
    return monkey_business(monkeys)


print("Part 1:", part_1())
print("Part 2:", part_2())
