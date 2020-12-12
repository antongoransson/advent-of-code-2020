from itertools import product

FREE = 'L'
FLOOR = '.'
OCCUPIED = '#'

def get_neighbours(grid, p2 = False):
    n = {}
    r_l = len(grid)
    c_l = len(grid[0])
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            n[r, c] = []
            for dr, dc in product([-1, 0, 1], repeat = 2):
                if dr == 0 and dc == 0:
                    continue
                n_r = r + dr
                n_c = c + dc
                while n_r in range(r_l) and n_c in range(c_l) and grid[n_r][n_c] == FLOOR and p2:
                    n_r += dr
                    n_c += dc
                if n_r in range(r_l) and n_c in range(c_l):
                    n[r, c].append((n_r, n_c))
    return n

def get_next_state(pos, seats, neighbours, p2 = False):
    n_occupied = 0
    n_occupied = len([1 for r, c in neighbours[pos] if seats[r][c] == OCCUPIED])
    r, c = pos
    if seats[r][c] == FREE and n_occupied == 0:
        return OCCUPIED
    elif seats[r][c] == OCCUPIED and n_occupied >= (4 + p2):
        return FREE
    return seats[r][c]

def solve_part_1(seats):
    neighbours = get_neighbours(seats)
    next_seats = []
    while True:
        n = 0
        for r, row in enumerate(seats):
            next_seats.append([get_next_state((r, c), seats, neighbours) for c in range(len(row))])
            n += len([1 for old_seat, new_seat in zip(row, next_seats[-1]) if old_seat != new_seat])
        seats = next_seats
        if n == 0:
            return sum([c == OCCUPIED for row in seats for c in row])
        next_seats = []

def solve_part_2(seats):
    neighbours = get_neighbours(seats, True)
    next_seats = []
    while True:
        n = 0
        for r, row in enumerate(seats):
            next_seats.append([get_next_state((r, c), seats, neighbours, True) for c in range(len(row))])
            n += len([1 for old_seat, new_seat in zip(row, next_seats[-1]) if old_seat != new_seat])
        seats = next_seats
        if n == 0:
            return sum([c == OCCUPIED for row in seats for c in row])
        next_seats = []


def main():
    seats = []
    with open('input.txt') as f:
        seats = [[c for c in line if c.strip()] for line in f]
    sol1 = solve_part_1(seats)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(seats)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
