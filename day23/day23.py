def play(current, cups, i):
    for _ in range(i):
        p1 = cups[current]
        p2 = cups[p1]
        p3 = cups[p2]
        dest_cup = current - 1 if current > 1 else len(cups)
        while dest_cup == p1 or dest_cup == p2 or dest_cup == p3:
            dest_cup = dest_cup - 1 if dest_cup > 1 else len(cups)
        dest_next = cups[dest_cup]
        cups[dest_cup] = p1
        cups[current] = cups[p3]
        cups[p3] = dest_next
        current = cups[current]
    return cups

def solve_part_1(cc, cups):
    cups = play(cc, cups, 100)
    c = 1
    s = ''
    for _ in range(len(cups) - 1):
        c = cups[c]
        s += str(c)
    return s


def solve_part_2(cc, cups):
    cups = play(cc, cups, 10000000)
    return int(cups[1]) * int(cups[cups[1]])
    

def main():
    in_data = list(map(int, '362981754'))
    cups = { in_data[i]:  in_data[(i + 1) % len(in_data)] for i in range(len(in_data))}
    cc = in_data[0]
    sol1 = solve_part_1(cc, cups)
    print('Part 1: {}'.format(sol1))

    in_data += [i for i in range(10, 1000000 + 1)]
    cups = { in_data[i]:  in_data[(i + 1) % len(in_data)] for i in range(len(in_data))}
    sol2 = solve_part_2(cc, cups)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
