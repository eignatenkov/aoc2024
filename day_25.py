import numpy as np

with open("data/day_25.txt") as f:
    keys = []
    locks = []
    cur_pattern = []
    for line in f:
        line = line.strip()
        if line == "":
            kl = np.array(cur_pattern)
            if np.all(kl[0] == '#'):
                locks.append(np.sum(kl[1:] == '#', axis=0))
            else:
                keys.append(np.sum(kl[:-1] == '#', axis=0))
            cur_pattern = []
        else:
            cur_pattern.append(list(line))
    kl = np.array(cur_pattern)
    if np.all(kl[0] == '#'):
        locks.append(np.sum(kl[1:] == '#', axis=0))
    else:
        keys.append(np.sum(kl[:-1] == '#', axis=0))

# print(keys)
# print(locks)
matching_pairs = 0
for k in keys:
    for l in locks:
        if np.all(k + l < 6):
            matching_pairs += 1
print(matching_pairs)