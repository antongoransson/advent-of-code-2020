from functools import reduce
from operator import mul
import regex as re

def calc_n_trees(slope, grid):
    dc, dr = slope
    return len([r for r in range(1, len(grid) // dx) if grid[r * dx][r * dy % len(grid[r])] == '#'])

def solve_part_1(grid):
    return calc_n_trees((3, 1), grid)

def solve_part_2(grid):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return reduce(mul, [calc_n_trees(s, grid) for s in slopes])

def main():
    with open('input.txt') as f:
        grid = [line.strip() for line in f]
    sol1 = solve_part_1(grid)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(grid)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
