import numpy as np
import re
from tqdm import tqdm

with open("data/day_14.txt") as f:
    robots = []
    for line in f:
        x, y, v_x, v_y = map(int, re.findall(r'-*\d+', line))
        robots.append((x, y, v_x, v_y))

BOARD_X = 101
BOARD_Y = 103
# BOARD_X = 11
# BOARD_Y = 7

def make_move(x, y, v_x, v_y, n_moves):
    new_x = (x + n_moves * v_x) % BOARD_X
    new_y = (y + n_moves * v_y) % BOARD_Y
    return new_x, new_y

new_positions = []
for x, y, v_x, v_y in robots:
    new_positions.append(make_move(x, y, v_x, v_y, 100))

# print(new_positions)

quadrants = [0, 0, 0, 0]
for x, y in new_positions:
    if x < BOARD_X // 2:
        if y < BOARD_Y // 2:
            quadrants[0] += 1
        elif y > BOARD_Y // 2:
            quadrants[3] += 1
    elif x > BOARD_X // 2:
        if y < BOARD_Y // 2:
            quadrants[1] += 1
        elif y > BOARD_Y // 2:
            quadrants[2] += 1

print(np.prod(np.array(quadrants)))

def make_move_robots(robots):
    new_robots = []
    for x, y, v_x, v_y in robots:
        new_x, new_y = make_move(x, y, v_x, v_y, 1)
        new_robots.append((new_x, new_y, v_x, v_y))
    return new_robots

def find_robots_size(robots, margins=100):
    r_x = sorted([r[0] for r in robots])
    r_y = sorted([r[1] for r in robots])
    return r_x[-margins] - r_x[margins], r_y[-margins] - r_y[margins]

def print_robots(robots):
    board = np.zeros((BOARD_Y, BOARD_X), dtype=int)
    for x, y, v_x, v_y in robots:
        board[y, x] = 1
    for y in range(BOARD_Y):
        print(''.join(map(str, board[y])))


for i in tqdm(range(1, 100000)):
    robots = make_move_robots(robots)
    r_x, r_y = find_robots_size(robots)
    if r_x < 30 and r_y < 30:
        print(i)
        print_robots(robots)
        break