import math

def get_seat_n(seat_n):
    row_n = seat_n[:7].replace('F', '0').replace('B', '1')
    col_n = seat_n[-3:].replace('L', '0').replace('R','1')
    return int(row_n, 2) * 8  + int(col_n, 2)

def solve_part_1(seats):
    return max([get_seat_n(seat) for seat in seats])

def solve_part_2(seats):
    seat_ids = set([get_seat_n(seat) for seat in seats])
    for i in seat_ids:
        if i + 1 not in seat_ids and i + 2 in seat_ids:
            return i + 1


def main():
    with open('input.txt') as f:
        seats = [line.strip() for line in f.readlines()]
    sol1 = solve_part_1(seats)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(seats)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
