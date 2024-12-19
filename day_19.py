from functools import lru_cache


with open("data/day_19.txt") as f:
    towels = tuple(f.readline().strip().split(', '))
    designs = []
    for line in f:
        if line.strip():
            designs.append(line.strip())


def is_design_possible(design, towels):
    for towel in towels:
        if towel == design:
            return True
        if design.startswith(towel):
            if is_design_possible(design[len(towel):], towels):
                return True
    return False

@lru_cache(maxsize=1000000)
def count_arrangements(design, towels):
    total_ways = 0
    for towel in towels:
        if towel == design:
            total_ways += 1
        if design.startswith(towel):
            total_ways += count_arrangements(design[len(towel):], towels)
    return total_ways


print(sum(is_design_possible(d, towels) for d in designs))
print(sum(count_arrangements(d, towels) for d in designs))
