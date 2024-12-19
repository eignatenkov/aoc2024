from functools import lru_cache
with open("data/day_11.txt") as f:
    stones = list(map(int, f.read().strip().split()))

@lru_cache(maxsize=1000000)
def count_stones(stone, n_steps):
    if n_steps == 0:
        return 1
    if stone == 0:
        return count_stones(1, n_steps - 1)
    if not len(str(stone)) % 2:
        return count_stones(int(str(stone)[:(len(str(stone)) // 2)]), n_steps-1) + count_stones(int(str(stone)[(len(str(stone)) // 2):]), n_steps-1)
    return count_stones(stone * 2024, n_steps - 1)

print(sum(count_stones(stone, 25) for stone in stones))
print(sum(count_stones(stone, 75) for stone in stones))