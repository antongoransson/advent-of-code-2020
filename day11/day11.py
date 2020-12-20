from itertools import product
from collections import defaultdict

def get_neighbours(seats, row_l, col_l, p2):
    all_neighbours = {}
    for pos in seats:
        r, c = pos 
        neighbours = set()
        for dr, dc in product([-1, 0, 1], repeat = 2):
            if dr == 0 and dc == 0:
                continue
            n_r = r + dr
            n_c = c + dc
            new_pos = (n_r, n_c)
            while p2 and n_r in range(row_l) and n_c in range(col_l) and new_pos not in seats:
                n_r += dr
                n_c += dc
                new_pos = (n_r, n_c)
            if new_pos in seats:
                neighbours.add(new_pos)
        all_neighbours[pos] = neighbours
    return all_neighbours

def next_state(pos, seats, n_occupied, p2 = False):
    if seats[pos] == 'L' and n_occupied == 0:
        return '#'
    elif seats[pos] == '#' and n_occupied >= (4 + p2):
        return 'L'
    return seats[pos]

def solve_problem(seats, row_l = None, col_l = None, p2 = False):
    neighbours = get_neighbours(seats, row_l, col_l, p2)
    while True:
        n_occupied = defaultdict(int)
        changed = False
        next_seats = {}
        for pos in seats:
            for n in neighbours[pos]:
                if seats[n] == '#':
                    n_occupied[pos] += 1
            next_seats[pos] = next_state(pos, seats, n_occupied[pos], p2)
            if seats[pos] != next_seats[pos]:
                changed = True
        seats = next_seats
        if not changed:
            return(sum([seat == '#' for seat in seats.values()]))

def solve_part_1(seats, row_l, col_l):
    return solve_problem(seats)

def solve_part_2(seats, row_l, col_l):
    return solve_problem(seats, row_l, col_l, True)

def main():
    seats = {}
    row_l, col_l = 0, 0
    with open('input.txt') as f:
        for r, line in enumerate(f):
            row_l += 1
            col_l = len(line.strip())
            for c, p in enumerate(line):
                if p == 'L':
                    seats[r, c] = p
    sol1 = solve_part_1(seats, row_l, col_l)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(seats, row_l, col_l)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
