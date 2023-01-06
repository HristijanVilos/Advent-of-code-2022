class Cube:
    def __init__(self, cube: list[str]) -> None:
        self.x = int(cube[0])
        self.y = int(cube[1])
        self.z = int(cube[2])

    def __repr__(self) -> str:
        return f"x:{self.x}, y:{self.y}, z:{self.z}"


    def have_adjacent_side(self, other) -> bool:
        if self.x + 1 == other.x or self.x == other.x + 1:
            if self.y == other.y and self.z == other.z:
                return True
        if self.y + 1 == other.y or self.y == other.y + 1:
            if self.x == other.x and self.z == other.z:
                return True
        if self.z + 1 == other.z or self.z == other.z + 1:
            if self.x == other.x and self.y == other.y:
                return True
        return False


def calculate_total_sides(number_of_cubes: int):
    return 6*number_of_cubes


def find_air_pocets():
    pass


def parse():
    with open("input.txt", "r") as file:
        return [Cube(line.strip().split(",")) for line in file]


def part_1(cubes: list[Cube]):
    count = 0
    for i in range(len(cubes)):
        for j in range(i+1, len(cubes)):
            if cubes[i].have_adjacent_side(cubes[j]):
                count += 1

    total_sides = calculate_total_sides(len(cubes))

    return (total_sides - 2*count)


def part_2(cubes: list[Cube]):
    pass


cubes = parse()
print("Part 1:", part_1(cubes))
print("Part 2:", part_2(cubes))
