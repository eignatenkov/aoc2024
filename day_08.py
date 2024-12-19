import numpy as np
from itertools import combinations
from math import gcd


with open("data/day_08.txt") as f:
    rows = list(map(lambda x: list(x), f.read().splitlines()))
    map = np.array(rows)
    items = set().union(*rows) - {'.'}


def find_antinodes(a, b):
    a_x, a_y = a
    b_x, b_y = b
    return {(2*a_x - b_x, 2* a_y - b_y), (2*b_x - a_x, 2* b_y - a_y)}

def point_on_map(a, board_shape):
    return 0 <= a[0] < board_shape[0] and 0 <= a[1] < board_shape[1]

def find_all_antinodes(a, b, board_shape):
    a_x, a_y = a
    b_x, b_y = b
    axis_gcd = gcd(abs(a_x - b_x), abs(a_y - b_y))
    x_step = a_x - b_x // axis_gcd
    y_step = a_y - b_y // axis_gcd

    antinodes = {tuple(a)}
    i = 1
    while True:
        antinode = (a_x + i * x_step, a_y + i * y_step)
        if point_on_map(antinode, board_shape):
            antinodes.add(antinode)
            i += 1
        else:
            break
    i = 1
    while True:
        antinode = (a_x - i * x_step, a_y - i * y_step)
        if point_on_map(antinode, board_shape):
            antinodes.add(antinode)
            i += 1
        else:
            break
    return antinodes



antinodes = set()
for i in items:
    antennas = np.argwhere(map == i)
    for a, b in combinations(antennas, 2):
        antinodes |= find_antinodes(a, b)

antinodes = {a for a in antinodes if point_on_map(a, map.shape)}
# print(antinodes)
print(len(antinodes))

antinodes = set()
for i in items:
    antennas = np.argwhere(map == i)
    for a, b in combinations(antennas, 2):
        antinodes |= find_all_antinodes(a, b, map.shape)
print(len(antinodes))
