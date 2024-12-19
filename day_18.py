import numpy as np
import heapq
from tqdm import tqdm


def neighbours(coords, graph_shape):
    c_x, c_y = coords
    dumb_neigbors = [(c_x - 1, c_y), (c_x + 1, c_y), (c_x, c_y - 1), (c_x, c_y + 1)]
    return [n for n in dumb_neigbors if 0 <= n[0] < graph_shape[0] and 0 <= n[1] < graph_shape[1]]


def heap_cheapest_path(graph):
    x = set()
    h = []
    costs = np.ones(list(graph.shape), dtype=int) * 10000
    costs[0, 0] = 0
    for i in range(costs.shape[0]):
        for j in range(costs.shape[1]):
            if graph[i, j] != 1:
                heapq.heappush(h, (costs[i, j], (i, j)))
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
        w_neighbours = neighbours(w, graph.shape)
        for n in w_neighbours:
            if n not in x and graph[n] != 1:
                new_key = key + 1
                heapq.heappush(h, (new_key, n))
    return costs

with open("data/day_18.txt") as f:
    falls = []
    for line in f:
        x, y = map(int, line.strip().split(','))
        falls.append((x, y))

MAP_SIZE = 71
FIRST_TASK_BYTES = 1024
maze = np.zeros((MAP_SIZE, MAP_SIZE), dtype=int)
for b in falls[:FIRST_TASK_BYTES]:
    maze[b] = 1

print(heap_cheapest_path(maze)[-1, -1])

maze = np.zeros((MAP_SIZE, MAP_SIZE), dtype=int)
for b in tqdm(falls):
    maze[b] = 1
    if heap_cheapest_path(maze)[-1, -1] == 10000:
        print(b)
        break