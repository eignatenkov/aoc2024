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
print(z_number)
print(int(z_number, 2))