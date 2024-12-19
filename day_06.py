import numpy as np
import time

with open("data/day_06.txt") as f:
    lines = []
    map_dict = {'.': 0, '#': 1, '^': 2}
    for line in f:
        lines.append(list(map(lambda x: map_dict[x], list(line.strip()))))
    board = np.array(lines)

start_x, start_y = np.argwhere(board == 2)[0]


def on_board(x, y, board):
    z, t = board.shape
    return 0 <= x < z and 0 <= y < t

def move_once(x, y, direction):
    if direction == 0:
        new_x, new_y = x - 1, y
    elif direction == 1:
        new_x, new_y = x, y + 1
    elif direction == 2:
        new_x, new_y = x + 1, y
    else:
        new_x, new_y = x, y - 1
    return new_x, new_y


def make_move(x, y, direction, board):
    try_moving = True
    while try_moving:
        new_x, new_y = move_once(x, y, direction)
        if on_board(new_x, new_y, board) and board[new_x, new_y] == 1:
            direction = (direction + 1) % 4
        else:
            try_moving = False
    return new_x, new_y, direction


positions = set()
direction = 0
cur_x, cur_y = start_x, start_y
while True:
    positions.add((cur_x, cur_y))
    cur_x, cur_y, direction = make_move(cur_x, cur_y, direction, board)
    if not on_board(cur_x, cur_y, board):
        break

print(len(positions))

def has_loop(board):
    cur_x, cur_y = np.argwhere(board == 2)[0]
    direction = 0
    positions = set()
    while True:
        new_element = (cur_x, cur_y, direction)
        if new_element in positions:
            return True
        else:
            positions.add(new_element)
        cur_x, cur_y, direction = make_move(cur_x, cur_y, direction, board)
        if not on_board(cur_x, cur_y, board):
            return False


loop_positions = set()
cur_x, cur_y = start_x, start_y
direction = 0
time_before = time.time()
while True:
    cur_x, cur_y, direction = make_move(cur_x, cur_y, direction, board)
    if on_board(cur_x, cur_y, board):
        if (cur_x, cur_y) != (start_x, start_y):
            new_board = np.copy(board)
            new_board[cur_x, cur_y] = 1
            if has_loop(new_board):
                loop_positions.add((cur_x, cur_y))
    else:
        break

print(len(loop_positions))
print(time.time() - time_before)