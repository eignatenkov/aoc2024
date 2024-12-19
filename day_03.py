import re


with open("data/day_03.txt") as f:
    memory = f.read()

def find_instructions(memory):
    return re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', memory)

def process_entry(entry):
    a, b = map(int, entry.strip('mul()').split(','))
    return a * b

print(sum(process_entry(memory) for memory in find_instructions(memory)))

def find_instructions_and_conditions(memory):
    return re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', memory)

# memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

new_instructions = find_instructions_and_conditions(memory)

print(new_instructions)

counter = 0
process = True
for i in new_instructions:
    if i == 'do()':
        process = True
    elif i == "don't()":
        process = False
    else:
        if process:
            counter += process_entry(i)
print(counter)