from tqdm import tqdm
A = 52884621
B = 0
C = 0
POINTER = 0
OUTPUT = []

program = [2,4,1,3,7,5,4,7,0,3,1,5,5,5,3,0]
# program = [0,3,5,4,3,0]
program_string = ','.join(map(str, program))

def combo_operand(value):
    global A, B, C
    if value <=3:
        return value
    if value == 4:
        return A
    if value == 5:
        return B
    if value == 6:
        return C

def do_instruction(instruction, operand):
    global A, B, C, POINTER, OUTPUT
    if instruction == 0:
        A = A // 2**combo_operand(operand)
    elif instruction == 1:
        B = B ^ operand
    elif instruction == 2:
        B = combo_operand(operand) % 8
    elif instruction == 3:
        if A != 0:
            POINTER = operand - 2
    elif instruction == 4:
        B = B ^ C
    elif instruction == 5:
        OUTPUT.append(combo_operand(operand) % 8)
    elif instruction == 6:
        B = A // 2**combo_operand(operand)
    elif instruction == 7:
        C = A // 2**combo_operand(operand)
    POINTER += 2


while POINTER < len(program):
    do_instruction(program[POINTER], program[POINTER + 1])

print(','.join(map(str, OUTPUT)))

def find_next_options(current):
    global A, B, C, POINTER, OUTPUT
    base = current * 8
    options = []
    for j in range(8):
        A = base + j
        B = 0
        C = 0
        POINTER = 0
        OUTPUT = []
        while POINTER < len(program):
            do_instruction(program[POINTER], program[POINTER + 1])
        str_output = ','.join(map(str, OUTPUT))
        if str_output == program_string[-len(str_output):]:
            options.append(base + j)
    return options

current_options = [0]
for i in range(16):
    next_options = []
    for c in current_options:
        next_options.extend(find_next_options(c))
    current_options = next_options

print(min(current_options))

