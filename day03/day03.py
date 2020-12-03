from functools import reduce
from operator import mul

def calc_n_trees(slope, grid):
    return len ([r for n_steps, r in zip(range(1, len(grid)), range(slope[1], len(grid), slope[1])) if grid[r][n_steps * slope[0] % len(grid[r])] == '#'])

    return calc_n_trees((3, 1), grid)

def solve_part_2(grid):
    return reduce(mul, [calc_n_trees(s, grid) for s in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])

def main():
    with open('input.txt') as f:
        grid = [line.strip() for line in f]
    sol1 = solve_part_1(grid)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(grid)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
