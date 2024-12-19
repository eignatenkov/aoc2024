from collections import defaultdict

with open("data/day_05.txt") as f:
    rules = defaultdict(set)
    updates = []
    for line in f:
        line = line.strip()
        if '|' in line:
            a, b = map(int,line.split('|'))
            rules[a].add(b)
        elif ',' in line:
            updates.append(list(map(int, line.split(','))))

def check_update(update, rules):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[i] in rules[update[j]]:
                return False
    return True

def fix_update(update, rules):
    if check_update(update, rules):
        return update
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[i] in rules[update[j]]:
                update[j], update[i] = update[i], update[j]
                return fix_update(update, rules)

result = 0
result_2 = 0
for update in updates:
    if check_update(update, rules):
        result += update[len(update) // 2]
    else:
        new_update = fix_update(update, rules)
        result_2 += new_update[len(new_update) // 2]
print(result)
print(result_2)
