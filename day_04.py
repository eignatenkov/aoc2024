import numpy as np


raw_matrix = []
with open('data/day_04.txt') as f:
    for line in f:
        raw_matrix.append(list(line.strip()))

matrix = np.array(raw_matrix)

def check_index(matrix, i, j):
    x, y = matrix.shape
    candidates = []
    if i < x - 3:
        candidates.append(matrix[i:i+4, j])
        if j < y -3:
            candidates.append(matrix[np.arange(i,i+4), np.arange(j, j+4)])
        if j > 2:
            candidates.append(matrix[np.arange(i,i+4), np.arange(j, j-4, -1)])
    if i > 2:
        candidates.append(matrix[np.arange(i, i - 4, -1), j])
        if j < y -3:
            candidates.append(matrix[np.arange(i, i - 4, -1), np.arange(j,j+4)])
        if j > 2:
            candidates.append(matrix[np.arange(i, i - 4, -1), np.arange(j, j-4, -1)])
    if j < y - 3:
        candidates.append(matrix[i, j:j + 4])
    if j > 2:
        candidates.append(matrix[i, np.arange(j, j-4, -1)])
    return sum(''.join(list(c)) == "XMAS" for c in candidates)

def check_diag(matrix, i, j):
    x, y = matrix.shape
    if i in (0, x -1) or j in (0, y -1):
        return False
    d_one = matrix[np.arange(i-1, i+2), np.arange(j-1, j+2)]
    d_two = matrix[np.arange(i-1, i+2), np.arange(j+1, j-2, -1)]
    return ''.join(d_one) in {'MAS', 'SAM'} and ''.join(d_two) in {'MAS', 'SAM'}


print(sum(check_index(matrix, *ind) for ind in np.argwhere(matrix == 'X')))
print(sum(check_diag(matrix, *ind) for ind in np.argwhere(matrix == 'A')))
