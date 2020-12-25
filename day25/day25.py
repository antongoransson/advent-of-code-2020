def get_loop_size(pk):
    loop_size = 0
    n = 1
    while n != pk:
        loop_size += 1
        n = pow(7, loop_size, 20201227)
    return loop_size

def solve_part_1(card_pk, door_pk):
    loop_size = get_loop_size(card_pk)
    return pow(door_pk, loop_size , 20201227)


def main():
    with open('input.txt') as f:
        card_pk, door_pk = [int(line.strip()) for line in f]
    sol1 = solve_part_1(card_pk, door_pk)
    print('Part 1: {}'.format(sol1))


if __name__ == "__main__":
    main()
