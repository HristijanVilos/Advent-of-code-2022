def get_file_sizes(data: dict):
    result = 0
    list_of_dirs = [[key] + [val] for key, val in data.items()]
    for dir in list_of_dirs:
        for _dir in list_of_dirs:
            if _dir == dir:
                continue
            if dir[0] in _dir[0]:
                dir[1] += _dir[1]
        if dir[1] < 100000:
            result += dir[1]
    return list_of_dirs, result


def get_filesystem_with_sizes(file):
    filesysytem = {}
    where_am_i = []
    for line in file:
        if line.strip().startswith("$ cd"):
            cd = line.split(" ")[2].strip()
            if cd == "..":
                where_am_i.pop()
                continue
            if not where_am_i:
                filesysytem[cd] = {}
                where_am_i.append(cd)
                continue
            else:
                where_am_i.append(cd)
                pwd = "".join(where_am_i)
                filesysytem[pwd] = {}
        elif line.strip().startswith("$ ls"):
            continue
        else:
            pwd = "".join(where_am_i)
            f = line.strip().split(" ")
            if not filesysytem[pwd]:
                filesysytem[pwd] = 0
            if f[0].isnumeric():
                filesysytem[pwd] += int(f[0])

    return get_file_sizes(filesysytem)


def part_1():
    with open("input.txt", "r") as file:
        list_of_dirs, result = get_filesystem_with_sizes(file)
        return result


def part_2():
    with open("input.txt", "r") as file:
        list_of_dirs, result = get_filesystem_with_sizes(file)
        list_of_dirs.sort(key=lambda x: x[1])
        used_space = list_of_dirs.pop()[1]
        needed_space = 30000000 - (70000000 - used_space)
        return next(x[1] for x in list_of_dirs if x[1] > needed_space)


print("Part 1:", part_1())
print("Part 2:", part_2())
