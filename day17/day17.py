from collections import Counter
from itertools import product
from copy import deepcopy

def solve_problem(grid):
    for _ in range(6):
        # Only consider neighbours of active cubes
        active_count = Counter([n for pos in grid for n in get_neighbours(pos)])
        new_grid = set([pos for pos, n in active_count.items() if next_state(pos, grid, n)])
        grid = new_grid
    return len(grid)

def get_neighbours(pos):
    neighbours = set()
    for deltas in product([-1, 0, 1], repeat = len(pos)):
        if all([d == 0 for d in deltas]):
            continue
        neighbours.add(tuple([n + d for n, d in zip(pos, deltas)]))
    return neighbours


def next_state(pos, grid, n_active):
    if pos in grid and n_active in (2, 3):
        return True
    elif pos not in grid and n_active == 3:
        return True
    return False
    

def solve_part_1(grid):
    return solve_problem(grid)

def solve_part_2(grid_part_2):
    return solve_problem(grid_part_2)

def main():
    w, z = 0, 0
    grid_part_1 = set()
    grid_part_2 = set()
    with open('input.txt') as f:
        for r, line in enumerate(f):
            for c, c_val in enumerate(line.strip()):
                if c_val == '#':
                    grid_part_1.add((z, r, c))
                    grid_part_2.add((w, z, r, c))
    sol1 = solve_part_1(grid_part_1)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(grid_part_2)
    print('Part 2: {}'.format(sol2))

if __name__ == "__main__":
    main()
