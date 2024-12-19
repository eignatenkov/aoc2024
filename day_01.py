import numpy as np
from collections import Counter

a_list = []
b_list = []

with open("data/day_01.txt") as f:
    for line in f:
        a, b = map(int, line.split())
        a_list.append(a)
        b_list.append(b)

a_list = np.array(a_list)
b_list = np.array(b_list)

print(np.abs(np.sort(a_list) - np.sort(b_list)).sum())

b_counter = Counter(b_list)

print(sum(a * b_counter.get(a, 0) for a in a_list))