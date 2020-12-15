from collections import defaultdict
from itertools import combinations
import regex as re

def find_number(numbers):
    n = 25
    for i in range(n, len(numbers)):
        found = any([a + b == numbers[i] for a, b in combinations(numbers[i - n: i], 2)])
        if not found:
            return numbers[i]

def solve_part_1(numbers):
    return find_number(numbers)

def solve_part_2(numbers):
    n = find_number(numbers)
    sums = defaultdict(list)
    for i in range(len(numbers)):
        for k in sums.keys():
            sums[k].append(numbers[i])
            if sum(sums[k]) > n:
                del sums[k]
            if sum(sums[k]) == n:
                return min(sums[k]) + max(sums[k])
        sums[i].append(numbers[i])


def main():
    with open('input.txt') as f:
        in_data = list(map(int, re.findall(r'-?\d+', f.read())))
    sol1 = solve_part_1(in_data)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(in_data)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
