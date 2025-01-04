def read_input():
    with open ("data/day_24.txt") as f:
        nodes = dict()
        rules = set()
        for line in f:
            if ':' in line:
                k, v = line.strip().split(': ')
                nodes[k] = int(v)
            elif ' -> ' in line:
                r, target = line.strip().split(' -> ')
                a, op, b = r.split(' ')
                rules.add((a, b, op, target))
    return rules, nodes

rules, nodes = read_input()

while rules:
    r = rules.pop()
    a, b, op, target = r
    if a in nodes and b in nodes:
        if op == 'AND':
            nodes[target] = nodes[a] & nodes[b]
        elif op == 'OR':
            nodes[target] = nodes[a] | nodes[b]
        elif op == 'XOR':
            nodes[target] = nodes[a] ^ nodes[b]
    else:
        rules.add(r)


zs = {k: v for k, v in nodes.items() if k.startswith('z')}
z_number = ''
for i in range(len(zs)):
    z_number = str(zs[f'z{i:02}']) + z_number
print(int(z_number, 2))

rules, nodes = read_input()

import networkx as nx
import gravis as gv
import matplotlib.pyplot as plt
G = nx.DiGraph()
for rule in rules:
    clr = 'red' if rule[2] == 'XOR' else 'black'
    G.add_edge(rule[0], rule[3], color=clr)
    G.add_edge(rule[1], rule[3], color=clr)

gv.d3(G)

print(','.join(sorted(['qqp', 'z23', 'pbv', 'z16', 'qff', 'qnw', 'fbq', 'z36'])))