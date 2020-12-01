from itertools import combinations
from functools import reduce
from operator import mul
import regex as re


def get_expense(l, n):
    for c in combinations(l, n):
        if sum(c) == 2020:
            return reduce(mul, c)

def solve_part_1(l):
    return get_expense(l, 2)


def solve_part_2(l):
     return get_expense(l, 3)


def main():
    with open('input.txt') as f:
        in_data = list(map(int, re.findall(r'-?\d+', f.read())))
    sol1 = solve_part_1(in_data)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(in_data)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
