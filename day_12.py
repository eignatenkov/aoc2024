import numpy as np
from queue import SimpleQueue

with open("data/day_12.txt") as f:
    rows = []
    for line in f:
        rows.append(list(line.strip()))
    garden = np.array(rows, dtype=str)

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

def find_connected_component(i, j, garden_map):
    mark = garden_map[i, j]
    border = SimpleQueue()
    visited = set()
    border.put((i, j))
    while not border.empty():
        next_point = border.get()
        if next_point not in visited:
            visited.add(next_point)
            neighbours = get_neighbours(*next_point, garden_map)
            for point in neighbours:
                if point not in visited and garden_map[point] == mark:
                    border.put(point)
    return visited

def calc_perimeter(component, garden_map):
    if len(component) == 1:
        return 4
    a = component.pop()
    a_neighbors = set(get_neighbours(*a, garden_map)) & component
    return calc_perimeter(component, garden_map) + 4 - 2 * len(a_neighbors)

def calc_sides(component, garden_map):
    if len(component) == 1:
        return 4
    top_row = min(c[0] for c in component)
    left_most_top_row = min(c[1] for c in component if c[0] == top_row)
    a = (top_row, left_most_top_row)
    component.remove(a)
    a_neighbors = set(get_neighbours(*a, garden_map)) & component
    if len(a_neighbors) == 0:
        return 4 + calc_sides(component, garden_map)
    if len(a_neighbors) == 2:
        if (a[0] + 1, a[1] - 1) in component:
            return calc_sides(component, garden_map)
        else:
            return calc_sides(component, garden_map) - 2
    if (a[0], a[1] + 1) in component:
        if (a[0] + 1, a[1] + 1) in component:
            return calc_sides(component, garden_map) + 2
        else:
            return calc_sides(component, garden_map)
    if (a[0]+ 1, a[1] - 1) in component and (a[0] + 1, a[1] + 1) in component:
        return calc_sides(component, garden_map) + 4
    if (a[0] + 1, a[1] - 1) not in component and (a[0] + 1, a[1] + 1) not in component:
        return calc_sides(component, garden_map)
    return calc_sides(component, garden_map) + 2


non_visited = set((i, j) for i in range(garden.shape[0]) for j in range(garden.shape[1]))
components = []
while non_visited:
    i, j = non_visited.pop()
    new_component = find_connected_component(i, j, garden)
    components.append(new_component)
    non_visited -= new_component

print(sum(len(c) * calc_perimeter(c, garden) for c in components))

non_visited = set((i, j) for i in range(garden.shape[0]) for j in range(garden.shape[1]))
components = []
while non_visited:
    i, j = non_visited.pop()
    new_component = find_connected_component(i, j, garden)
    components.append(new_component)
    non_visited -= new_component

print(sum(len(c) * calc_sides(c, garden) for c in components))