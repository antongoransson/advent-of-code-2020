import math

def get_seat_n(seat_n):
    r_a = 0
    r_b = 127
    c_a = 0
    c_b = 7
    for c in seat_n:
        if c == 'F':
            r_b = r_b - math.ceil(((r_b - r_a) / 2))
        elif c == 'B':
            r_a = r_a + math.ceil((r_b - r_a) / 2)
        elif c == 'L':
            c_b = c_b - math.ceil(((c_b - c_a) / 2))
        elif c == 'R':
            c_a = c_a + math.ceil(((c_b - c_a) / 2))
    return r_a * 8 + c_a

def solve_part_1(seats):
    return max([get_seat_n(seat) for seat in seats])

def solve_part_2(seats):
    seat_numbers = set([get_seat_n(seat) for seat in seats])
    for row in range(2, 128):
        for col in range(0, 8):
            if row * 8 + col not in seat_numbers:
                return row * 8 + col


def main():
    with open('input.txt') as f:
        seats = [line for line in f.readlines()]
    sol1 = solve_part_1(seats)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(seats)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
