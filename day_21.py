import numpy as np
from collections import Counter

BEST_MAP = dict()


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def find_all_instructions(code, cur_pos='A', numeric=True):
    if numeric:
        keyboard = np.array([['7','8','9'],['4','5','6'], ['1','2','3'], ['#', '0', 'A']], dtype=str)
    else:
        keyboard = np.array([['#', '^', 'A'], ['<', 'v', '>']], dtype=str)
    if len(code) == 0:
        return ['']
    next_pos = code[0]
    if cur_pos == next_pos:
        return ['A' + c for c in find_all_instructions(code[1:], cur_pos=next_pos, numeric=numeric)]
    cur_x, cur_y = np.argwhere(keyboard == cur_pos)[0]
    new_x, new_y = np.argwhere(keyboard == next_pos)[0]
    if manhattan_distance((cur_x, cur_y), (new_x, new_y)) == 1:
        if new_x == cur_x + 1:
            move = 'v'
        elif new_x == cur_x - 1:
            move = '^'
        elif new_y == cur_y + 1:
            move = '>'
        else:
            move = '<'
        return [move + 'A' + i for i in find_all_instructions(code[1:], next_pos, numeric=numeric)]
    else:
        paths = []
        if new_x > cur_x and keyboard[cur_x + 1, cur_y] != '#':
            paths += ['v' + c for c in find_all_instructions(code, keyboard[cur_x + 1, cur_y], numeric=numeric)]
        elif new_x < cur_x and keyboard[cur_x - 1, cur_y] != '#':
            paths += ['^' + c for c in find_all_instructions(code, keyboard[cur_x - 1, cur_y], numeric=numeric)]
        if new_y > cur_y:
            paths += ['>' + c for c in find_all_instructions(code, keyboard[cur_x, cur_y + 1], numeric=numeric)]
        elif new_y < cur_y and keyboard[cur_x, cur_y - 1] != '#':
            paths += ['<' + c for c in find_all_instructions(code, keyboard[cur_x, cur_y - 1], numeric=numeric)]
        return paths


def instruction_to_dict(instruction):
    return Counter(j + 'A' for j in instruction[:-1].split('A'))

def len_dict_repr(dict_repr):
    return sum(len(k)*v for k, v in dict_repr.items())


def unroll_dict(instruction_dict):
    global BEST_MAP
    new_dict = Counter()
    for k, v in instruction_dict.items():
        if k not in BEST_MAP:
            BEST_MAP[k] = find_best_repr(k)
        for sub_words, n in BEST_MAP[k].items():
            new_dict[sub_words] += n * v
    return new_dict


def find_best_repr(subword):
    first_level = find_all_instructions(subword, numeric=False)
    best_repr = None
    min_len = float('inf')
    for fl in first_level:
        sl = find_all_instructions(fl, numeric=False)
        for s in sl:
            if len(s) <= min_len:
                min_len = len(s)
                best_repr = fl
    return instruction_to_dict(best_repr)

#287046661958274
def shortest_instruction(code, n_directional_iterations=2):
    global BEST_MAP
    first_reps = find_all_instructions(code, numeric=True)
    best_len = float('inf')
    for fr in first_reps:
        rep_dict = instruction_to_dict(fr)
        for i in range(n_directional_iterations):
            rep_dict = unroll_dict(rep_dict)
        len_rep = len_dict_repr(rep_dict)
        if len_rep < best_len:
            best_len = len_rep
    return best_len


# test_codes = ['029A', '980A', '179A', '456A', '379A']
test_codes = ['480A', '143A', '983A', '382A', '974A']
print(sum(int(code[:3]) * shortest_instruction(code, 2) for code in test_codes))
print(sum(int(code[:3]) * shortest_instruction(code, 25) for code in test_codes))
print(BEST_MAP)