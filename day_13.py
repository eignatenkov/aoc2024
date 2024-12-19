import re
import numpy as np


def parse_input(filename):
    machines = []
    with open(filename) as f:
        current_machine = [list(), list()]
        for line in f:
            if line.strip():
                x, y = map(int, re.findall(r'\d+', line))
                current_machine[0].append(x)
                current_machine[1].append(y)
            else:
                machines.append(current_machine)
                current_machine = [list(), list()]
        machines.append(current_machine)
    return machines

def prime_machine(x, y, prize):
    gcd = np.gcd(x, y)
    if prize % gcd != 0:
        raise "bad prize"
    return x // gcd, y // gcd, prize // gcd


def solve_single_min_x(x, y , prize, max_push=None):
    if max_push is None:
        max_push = np.inf
    x_multiplier = 0
    while x_multiplier <= max_push:
        y_part = prize - x * x_multiplier
        if y_part < 0:
            return None, None
        if y_part % y == 0 and y_part // y <= max_push:
            return x_multiplier, y_part // y
        x_multiplier += 1
    return None, None

def solve_big_machines(machine_a, machine_b, max_push=None):
    try:
        x_1, x_2, prize_1 = prime_machine(*machine_a)
        y_1, y_2, prize_2 = prime_machine(*machine_b)
    except:
        return -1
    k, l = solve_single_min_x(x_1, x_2, prize_1, max_push)
    m, n = solve_single_min_x(y_1, y_2, prize_2, max_push)
    if k is None or m is None:
        return -1
    if y_2 * x_1 == y_1 * x_2:
        return -1
    b = ((l - n) * x_2 + (k - m) * x_1) / (y_2 * x_1 - y_1 * x_2)
    if int(b) != b:
        return -1
    return int(3 * (m + b*y_2) + (n - b * y_1))


machines = parse_input("data/day_13.txt")

answer = 0
answer_2 = 0
for m_one, m_two in machines:
    ans = solve_big_machines(m_one, m_two, max_push=100)
    m_one[-1] += 10000000000000
    m_two[-1] += 10000000000000
    bans = solve_big_machines(m_one, m_two)
    if ans > 0:
        answer += ans
    if bans > 0:
        answer_2 += bans
print(answer, answer_2)
