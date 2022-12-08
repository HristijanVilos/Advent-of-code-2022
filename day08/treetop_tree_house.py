def visabilty(list_of_bools):
    for count, i in enumerate(list_of_bools):
        if not i:
            return count + 1
    return count + 1


def part_1():
    with open("input.txt", "r") as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))

        visable_trees = 0
        for i, row in enumerate(grid):
            for j, tree in enumerate(row):
                if i == 0 or i == len(grid) - 1\
                        or j == 0 or j == len(row) - 1:
                    visable_trees += 1
                    continue
                if (all(grid[i][tj] < tree for tj in range(0, j))
                        or all(grid[i][tj] < tree for tj in range(j+1, len(row)))
                        or all(grid[ti][j] < tree for ti in range(0, i))
                        or all(grid[ti][j] < tree for ti in range(i+1, len(grid)))):

                    visable_trees += 1

    return visable_trees


def part_2():
    with open("input.txt", "r") as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))

        max_visability = 0
        for i, row in enumerate(grid):
            for j, tree in enumerate(row):
                if i == 0 or i == len(grid) - 1\
                        or j == 0 or j == len(row) - 1:
                    continue
                left = visabilty([grid[i][tj] < tree for tj in range(j-1, -1, -1)])
                right = visabilty([grid[i][tj] < tree for tj in range(j+1, len(row))])
                up = visabilty([grid[ti][j] < tree for ti in range(i-1, -1, -1)])
                down = visabilty([grid[ti][j] < tree for ti in range(i+1, len(grid))])
                prod = (left * right * up * down)

                if prod > max_visability:
                    max_visability = prod
    return max_visability


print("Part 1:", part_1())
print("Part 2:", part_2())
