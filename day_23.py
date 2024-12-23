from collections import defaultdict

graph =defaultdict(list)
with open("data/day_23.txt") as f:
    for line in f:
        a, b = line.strip().split('-')
        graph[a].append(b)
        graph[b].append(a)


triangles = set()
for v, connections in graph.items():
    for second in connections:
        for third in graph[second]:
            if v in graph[third]:
                triangles.add(tuple(sorted((v, second, third))))

print(len([t for t in triangles if any(c.startswith('t') for c in t)]))


def find_fully_connect(vertices, graph):
    if len(vertices) == 1:
        return [vertices]
    if len(vertices) == 0:
        return []
    v = vertices.pop()
    v_neighbors = set(graph[v]) & (vertices - {v})
    return [{v} | ffc for ffc in find_fully_connect(v_neighbors, graph)] + find_fully_connect(vertices, graph)


max_component = set()
for v, neighbors in graph.items():
    ffcs = find_fully_connect({v} | set(neighbors), graph)
    for ffc in ffcs:
        if len(ffc) > len(max_component):
            max_component = ffc

print(','.join(sorted(max_component)))