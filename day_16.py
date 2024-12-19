import numpy as np
import heapq


with open("data/day_16.txt") as f:
    rows = []
    instructions = []
    for line in f:
        if line.startswith("#"):
            rows.append(list(line.strip()))
        elif line.strip():
            instructions += list(line.strip())
    maze = np.array(rows, dtype=str)[1:-1, 1:-1]


def print_board(board):
    for i in range(board.shape[0]):
        print(''.join(board[i]))


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

def next_direct_move(i, j, direction):
    if direction == 0:
        return i, j + 1
    elif direction == 1:
        return i + 1, j
    elif direction == 2:
        return i, j - 1
    elif direction == 3:
        return i -1, j

def previous_position(i, j, direction):
    if direction == 0:
        return i, j - 1, direction
    elif direction == 1:
        return i - 1, j, direction
    elif direction == 2:
        return i, j + 1, direction
    elif direction == 3:
        return i + 1, j, direction


def heap_cheapest_path(graph):
    x = set()
    h = []
    costs = np.ones(list(graph.shape) + [4], dtype=int) * 1000000
    costs[-1, 0, 0] = 0
    for i in range(costs.shape[0]):
        for j in range(costs.shape[1]):
            if graph[i, j] != '#':
                for k in range(costs.shape[2]):
                    heapq.heappush(h, (costs[i, j, k], (i, j, k)))
    while h:
        while True:
            if h:
                key, w = heapq.heappop(h)
                if w not in x:
                    break
            else:
                return costs
        x.add(w)
        costs[w] = key
        w_neighbors = [(w[0], w[1], (w[2] + 1) % 4), (w[0], w[1], (w[2] + 3) % 4)]
        for n in w_neighbors:
            if n not in x:
                new_key = key + 1000
                heapq.heappush(h, (new_key, n))
        w_next = next_direct_move(*w)
        if 0 <= w_next[0] < costs.shape[0] and 0 <= w_next[1] < costs.shape[1] and graph[w_next[0], w_next[1]] != '#':
            w_next = (w_next[0], w_next[1], w[2])
            if w_next not in x:
                new_key = key + 1
                heapq.heappush(h, (new_key, w_next))
    return costs


def find_sps(costs, position):
    x, y, z = position
    if x == costs.shape[0] - 1 and y == 0:
        return {(0, 0)}
    result = {(x, y)}
    for k in [(z + 1) % 4, (z + 3) % 4]:
        if costs[x, y, k] == costs[position] - 1000:
            result |= find_sps(costs, (x, y, k))
    prev_pos = previous_position(x, y, z)
    if 0 <= prev_pos[0] < costs.shape[0] and 0 <= prev_pos[1] < costs.shape[1] and costs[prev_pos] < costs[position]:
        result |= find_sps(costs, prev_pos)
    return result

costs = heap_cheapest_path(maze)
print(np.min(costs[0, -1]))
print(len(find_sps(costs, (0, maze.shape[1] - 1, np.argmin(costs[0, -1])))))