from copy import deepcopy


class Element:
    def __init__(self, id, val) -> None:
        self.id = id
        self.val = val

    def __repr__(self) -> str:
        return f"{self.val}"


def move_element(new_list: list, element: Element, len_list):
    index = next(i for i, n in enumerate(new_list) if n.id == element.id)
    del new_list[index]
    len_list = len_list - 1
    move = (index + element.val) % len_list
    new_list.insert(move, element)


def index_of_zero(new_list):
    return [i for i, n in enumerate(new_list) if n.val == 0][0]


def solution(sol=1, y=1):
    with open("input.txt", "r") as file:
        initial = [Element(id, int(line)*sol) for id, line in enumerate(file)]
        new_list = deepcopy(initial)
        len_inital = len(initial)

        for x in range(y):
            for i, ele in enumerate(initial):
                move_element(new_list, ele, len_inital)

        i = index_of_zero(new_list)
        result = 0
        result += new_list[(i+1000) % len_inital].val
        result += new_list[(i+2000) % len_inital].val
        result += new_list[(i+3000) % len_inital].val

    return result


print("Part 1:", solution())
print("Part 2:", solution(sol=811589153, y=10))
