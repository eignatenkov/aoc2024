import numpy as np


with open("data/day_15.txt") as f:
    rows = []
    instructions = []
    for line in f:
        if line.startswith("#"):
            rows.append(list(line.strip()))
        elif line.strip():
            instructions += list(line.strip())
    warehouse_map = np.array(rows, dtype=str)

def print_board(board):
    for i in range(board.shape[0]):
        print(''.join(board[i]))

def widen_board(board):
    new_rows = []
    for i in range(board.shape[0]):
        row = []
        for j in range(board.shape[1]):
            item = board[i][j]
            if item == "#":
                row.extend(['#', '#'])
            elif item == ".":
                row.extend(['.', '.'])
            elif item == "O":
                row.extend(['[', ']'])
            else:
                row.extend(["@", "."])
        new_rows.append(row)
    return np.array(new_rows, dtype=str)


def make_move(wm, instruction):
    r_pos = np.argwhere(wm == '@')[0]
    if instruction == '>':
        next_wall = np.argwhere(wm[r_pos[0], r_pos[1]:] == '#')[0][0]
        next_free = np.argwhere(wm[r_pos[0], r_pos[1]:] == '.')
        if len(next_free) == 0 or next_free[0][0] > next_wall:
            return
        next_free = next_free[0][0]
        wm[r_pos[0], r_pos[1] + 1:r_pos[1] + next_free + 1] = wm[r_pos[0], r_pos[1]: r_pos[1] + next_free]
        wm[r_pos[0], r_pos[1]] = '.'
    if instruction == 'v':
        ftm = find_figure_to_move(r_pos[0], r_pos[1], wm, move_down=True)
        move_figure(ftm, wm, move_down=True)
    if instruction == '<':
        next_wall = np.argwhere(wm[r_pos[0], r_pos[1]::-1] == '#')[0][0]
        next_free = np.argwhere(wm[r_pos[0], r_pos[1]::-1] == '.')
        if len(next_free) == 0 or next_free[0][0] > next_wall:
            return
        next_free = next_free[0][0]
        wm[r_pos[0], r_pos[1] - next_free:r_pos[1]] = wm[r_pos[0], r_pos[1] - next_free + 1: r_pos[1] + 1]
        wm[r_pos[0], r_pos[1]] = '.'
    if instruction == '^':
        ftm = find_figure_to_move(r_pos[0], r_pos[1], wm, move_down=False)
        move_figure(ftm, wm, move_down=False)


def find_figure_to_move(i, j, wm, move_down=True):
    ftm = {(i, j)}
    border_level = {(i, j)}
    while border_level:
        new_border = set()
        for x, y in border_level:
            nbx = (x + 1, y) if move_down else (x - 1, y)
            if wm[nbx] in {'O', '[', ']'}:
                new_border.add(nbx)
                if wm[nbx] == '[':
                    new_border.add((nbx[0], nbx[1] + 1))
                elif wm[nbx] == ']':
                    new_border.add((nbx[0], nbx[1] - 1))
        ftm |= new_border
        border_level = new_border
    return ftm

def move_figure(figure, board, move_down=True):
    new_position = {(x+1, y) for x, y in figure} if move_down else {(x-1, y) for x, y in figure}
    if any(board[np] == '#' for np in new_position):
        return
    figure_sorted = sorted(figure, reverse=move_down, key=lambda x: x[0])
    for x, y in figure_sorted:
        new_pos = (x + 1, y) if move_down else (x - 1, y)
        board[new_pos] = board[x, y]
        board[x, y] = '.'


wide_board = widen_board(warehouse_map)
for i in instructions:
    make_move(warehouse_map, i)

coord_sum = 0
for box in np.argwhere(warehouse_map == 'O'):
    coord_sum += 100 * box[0] + box[1]

print(coord_sum)

for i in instructions:
    make_move(wide_board, i)

coord_sum = 0
for box in np.argwhere(wide_board == '['):
    coord_sum += 100 * box[0] + box[1]

print(coord_sum)