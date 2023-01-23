def get_position(elf, move):
    e_m = elf[0] + move[0], elf[1] + move[1]
    if move[0] == 0:
        return (e_m[0]-1, e_m[1]), e_m, (e_m[0]+1, e_m[1])
    else:
        return (e_m[0], e_m[1]-1), e_m, (e_m[0], e_m[1]+1)


def elf_in_adjacent_position(elf, elves_pos):
    _moves = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1))
    for m in _moves:
        if (m[0] + elf[0], m[1] + elf[1]) in elves_pos:
            return True
    return False


def can_move_to(elf: tuple, elves_pos: set, moves):
    if elf_in_adjacent_position(elf, elves_pos):
        for move in moves:
            _moves = get_position(elf, move)
            can_move = True
            for m in _moves:
                if m in elves_pos:
                    can_move = False
                    break
            if can_move:
                return _moves[1]
    return elf


def draw_board(elves_pos):
    i = [x[0] for x in elves_pos]
    j = [x[1] for x in elves_pos]
    min_i, max_i = min(i), max(i)
    min_j, max_j = min(j), max(j)
    for _i in range(min_i, max_i+1):
        result_str = ""
        for _j in range(min_j, max_j+1):
            if (_i, _j) in elves_pos:
                result_str += "#"
            else:
                result_str += "."
        print(result_str)


def calc_emty_groun_tiles(elves_pos):
    i = [x[0] for x in elves_pos]
    j = [x[1] for x in elves_pos]
    min_i, max_i = min(i), max(i)
    min_j, max_j = min(j), max(j)
    resut = 0
    for _i in range(min_i, max_i+1):
        for _j in range(min_j, max_j+1):
            if (_i, _j) in elves_pos:
                continue
            resut += 1
    return resut


def solution():
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    with open("input.txt", "r") as file:
        elves_pos = {
            (i, j)
            for i, line in enumerate(file)
            for j, char in enumerate(line)
            if char == "#"
        }

        count = 0
        while True:
            suggested_pos = []
            keep_track = []
            # First part of the round
            for elf in elves_pos:
                pos = can_move_to(elf, elves_pos, moves)
                suggested_pos.append([pos, elf])
                keep_track.append(pos)

            # Second part of the round
            seen = set()
            dupes = [x for x in keep_track if x in seen or seen.add(x)]
            for pos in suggested_pos:
                if pos[0] in dupes:
                    pos[0] = pos[1]

            previous_round = elves_pos
            elves_pos = {x[0] for x in suggested_pos}

            # prepair moves for next round
            x = moves.pop(0)
            moves.append(x)
            count += 1
            if count == 10:
                print("Part 1:", calc_emty_groun_tiles(elves_pos))
            if previous_round == elves_pos:
                print("Part 2:", count)
                break


solution()
