import numpy as np
from itertools import chain
from functools import lru_cache
from tqdm import tqdm

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

@lru_cache(maxsize=1000000)
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


def shortest_instruction(code, n_directional_iterations=2):
    cur_it = find_all_instructions(code, numeric=True)
    for _ in tqdm(range(n_directional_iterations)):
        cur_it = list(chain.from_iterable(find_all_instructions(c, numeric=False) for c in cur_it))
        min_instr = min(len(s) for s in cur_it)
        cur_it = [c for c in cur_it if len(c) == min_instr]
    return min(len(c) for c in cur_it)


def type_code(code, numeric=True):
    if numeric:
        keyboard = np.array([['7','8','9'],['4','5','6'], ['1','2','3'], ['#', '0', 'A']], dtype=str)
    else:
        keyboard = np.array([['#', '^', 'A'], ['<', 'v', '>']], dtype=str)
    cur_pos = 'A'
    instructions = []
    for button in list(code):
        cur_x, cur_y = np.argwhere(keyboard == cur_pos)[0]
        new_x, new_y = np.argwhere(keyboard == button)[0]
        if new_y > cur_y:
            instructions += ['>'] * (new_y - cur_y)
            if new_x < cur_x:
                instructions += ['^'] * (cur_x - new_x)
            else:
                instructions += ['v'] * (new_x - cur_x)
        else:
            if new_x < cur_x:
                instructions += ['^'] * (cur_x - new_x)
            else:
                instructions += ['v'] * (new_x - cur_x)
            instructions += ['<'] * (cur_y - new_y)
        instructions.append('A')
        cur_pos = button
    return ''.join(instructions)

# test_codes = ['029A', '980A', '179A', '456A', '379A']
test_codes = ['480A', '143A', '983A', '382A', '974A']
print(sum(int(code[:3]) * shortest_instruction(code) for code in test_codes))
print(sum(int(code[:3]) * shortest_instruction(code, 5) for code in test_codes))
