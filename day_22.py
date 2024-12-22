import numpy as np
from collections import defaultdict

def update_number(number):
    number = ((number * 64) ^ number) % 16777216
    number = ((number // 32) ^ number) % 16777216
    number = ((number * 2048) ^ number) % 16777216
    return number


with open("data/day_22.txt") as f:
    buyers = []
    for line in f:
        buyers.append(int(line.strip()))

number_sum = 0
prices = []
for buyer in buyers:
    buyer_prices = np.zeros(2001)
    buyer_prices[0] = buyer % 10
    for i in range(2000):
        buyer = update_number(buyer)
        buyer_prices[i + 1] = buyer % 10
    number_sum += buyer
    prices.append(buyer_prices)
print(number_sum)

results = defaultdict(lambda: np.zeros(len(buyers)))
for i, buyer in enumerate(buyers):
    diffs = prices[i][1:] - prices[i][:-1]
    for j in range(2000 - 3):
        sequence = tuple(diffs[j:j + 4])
        if results[sequence][i] == 0:
            results[sequence][i] = prices[i][j + 4]

print(max(v.sum() for v in results.values()))
