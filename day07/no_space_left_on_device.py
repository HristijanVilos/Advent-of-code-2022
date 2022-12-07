result = 0
list_tuples = []


def get_nested(data, *args):
    if args and data:
        element = args[0]
        if element:
            value = data.get(element)
            return value if len(args) == 1 else get_nested(value, *args[1:])


def get_result(data):
    global result
    for k, v in data.items():
        if isinstance(v, int) and v <= 100000:
            result += v
        if isinstance(v, dict):
            get_result(v)


def get_file_sizes(data: dict, size=None):
    for v in data.values():
        if isinstance(v, int):
            size = v
        if isinstance(v, dict):
            if len(list(v.values())) == 1:
                data['size'] += v.get("size")
            else:
                x = get_file_sizes(v)
                data["size"] += x
            size = data["size"]
    return size


def get_filesystem_with_sizes(filesysytem, file):
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
                x = get_nested(filesysytem, *where_am_i)
                x[cd] = {}
                where_am_i.append(cd)
        elif line.strip().startswith("$ ls"):
            continue
        else:
            f = line.strip().split(" ")
            x = get_nested(filesysytem, *where_am_i)
            if not x.get("size"):
                x["size"] = 0
            if f[0].isnumeric():
                x = get_nested(filesysytem, *where_am_i)
                x["size"] += int(f[0])

    get_file_sizes(filesysytem["/"])


def get_directories_with_sizes(filesysytem):
    for k, v in filesysytem.items():
        if isinstance(v, dict):
            list_tuples.append(v["size"])
            get_directories_with_sizes(v)


def part_1():
    filesysytem = {}
    with open("input.txt", "r") as file:
        get_filesystem_with_sizes(filesysytem, file)
        get_result(filesysytem)

        return result


def part_2():
    filesysytem = {}
    with open("input.txt", "r") as file:
        get_filesystem_with_sizes(filesysytem, file)
        get_result(filesysytem)
        get_directories_with_sizes(filesysytem)
        empty_space = 70000000 - filesysytem['/']["size"]
        needed_space = 30000000 - empty_space
        list_tuples.sort()
        file_size = [x for x in list_tuples if x > needed_space][0]

        return file_size


print("Part 1:", part_1())
print("Part 2:", part_2())
