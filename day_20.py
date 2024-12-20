import numpy as np


with open("data/day_20.txt") as f:
    rows = []
    for line in f:
        rows.append(list(line.strip()))
    maze_map = np.array(rows, dtype=object)


def get_neighbours(i, j, hm):
    neighbours = []
    if i > 0:
        neighbours.append((i-1, j))
    if j > 0:
        neighbours.append((i, j - 1))
    if i < hm.shape[0] - 1:
        neighbours.append((i + 1, j))
    if j < hm.shape[1] - 1:
        neighbours.append((i, j + 1))
    return neighbours


start = np.argwhere(maze_map == 'S')[0]
cur_pos = start
maze_map[start[0], start[1]] = 0
i = 1
max_value = 0
go = True
while go:
    neighbours = get_neighbours(cur_pos[0], cur_pos[1], maze_map)
    for n in neighbours:
        if maze_map[n[0], n[1]] == '.':
            cur_pos = n
            maze_map[n[0], n[1]] = i
            i += 1
            break
        if maze_map[n[0], n[1]] == 'E':
            maze_map[n[0], n[1]] = i
            max_value = i
            go = False
            break

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def find_cheats(i, j, cheat_length, maze_map):
    cheats = set()
    for k in range(max(0, i - cheat_length), min(maze_map.shape[0], i + cheat_length + 1)):
        for l in range(max(0, j - cheat_length), min(maze_map.shape[1], j + cheat_length + 1)):
            if manhattan_distance((i, j), (k, l)) <= cheat_length and maze_map[k, l] != '#':
                cheats.add((k, l))
    return cheats


def count_effective_cheats(cheat_length, min_saved_time, maze_map, max_value):
    cheat_count = 0
    for track_position in range(max_value + 1):
        cur_pos = np.argwhere(maze_map == track_position)[0]
        cheats = find_cheats(cur_pos[0], cur_pos[1], cheat_length, maze_map)
        for c in cheats:
            new_distance = manhattan_distance(cur_pos, c)
            if maze_map[c[0], c[1]] - track_position - new_distance >= min_saved_time:
                cheat_count += 1
    return cheat_count

print(count_effective_cheats(2, 100, maze_map, max_value))
print(count_effective_cheats(20, 100, maze_map, max_value))
