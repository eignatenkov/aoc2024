import numpy as np

with open("data/day_10.txt") as f:
    rows = []
    for line in f:
        rows.append(list(map(int, list(line.strip()))))
    hike_map = np.array(rows)

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

def get_nines(i, j, hm):
    cur_value = hm[i, j]
    if cur_value == 9:
        return {(i,j)}
    nines = set()
    for n in get_neighbours(i, j, hm):
        if hm[n[0]][n[1]] == cur_value + 1:
            nines |= get_nines(n[0], n[1], hm)
    return nines

def count_trails(i, j, hm):
    cur_value = hm[i, j]
    if cur_value == 9:
        return 1
    trails = 0
    for n in get_neighbours(i, j, hm):
        if hm[n[0]][n[1]] == cur_value + 1:
            trails += count_trails(n[0], n[1], hm)
    return trails


print(sum(len(get_nines(z[0], z[1], hike_map)) for z in np.argwhere(hike_map == 0)))
print(sum(count_trails(z[0], z[1], hike_map) for z in np.argwhere(hike_map == 0)))