import numpy as np

with open("data/day_09.txt") as f:
    compressed_data = list(map(int, list(f.read().strip())))

frag_array = -1 * np.ones(sum(compressed_data), dtype=int)
cur_index = 0
for ind, val in enumerate(compressed_data):
    if not ind % 2:
        frag_array[cur_index:cur_index + val] = ind // 2
    cur_index += val

while (frag_array == -1).sum() > 0:
    ind_to_move = np.argwhere(frag_array >= 0).T[0][-1]
    place_to_move = np.argwhere(frag_array == -1)[0]
    frag_array[place_to_move] = frag_array[ind_to_move]
    frag_array = frag_array[:ind_to_move]

print(sum(a*i for i, a in enumerate(frag_array)))


frag_array = -1 * np.ones(sum(compressed_data), dtype=int)
cur_index = 0
for ind, val in enumerate(compressed_data):
    if not ind % 2:
        frag_array[cur_index:cur_index + val] = ind // 2
    cur_index += val

for block_value in range(frag_array.max(), 0, -1):
    block_length = len(np.where(frag_array == block_value)[0])
    block_indices = np.argwhere(frag_array == block_value)
    block_start = block_indices[0][0]
    empties = np.argwhere(frag_array[:block_start] == -1).T[0]
    for start in empties:
        if np.all(frag_array[start:start+block_length] == -1) and (start + block_length < len(frag_array)):
            frag_array[block_indices] = -1
            frag_array[start:start + block_length] = block_value
            break


frag_array[frag_array == -1] =0
print(sum(a*i for i, a in enumerate(frag_array)))
