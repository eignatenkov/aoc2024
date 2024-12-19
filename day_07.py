with open("data/day_07.txt") as f:
    data = []
    for line in f:
        test_value, numbers = line.strip().split(':')
        test_value = int(test_value)
        numbers = list(map(int, numbers.strip().split(' ')))
        data.append((test_value, numbers))

def find_solutions(numbers):
    if len(numbers) == 1:
        return set(numbers)
    return find_solutions([numbers[0] + numbers[1]] + numbers[2:]) | find_solutions([numbers[0] * numbers[1]] + numbers[2:]) | find_solutions([int(str(numbers[0]) + str(numbers[1]))] + numbers[2:])

print(len(data))

counter = 0
for tv, numbers in data:
    if tv in find_solutions(numbers):
        counter += tv

print(counter)