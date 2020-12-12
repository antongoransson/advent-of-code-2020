dd = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W'
}

navigate = {
    'N': lambda p, n: (p[0] - n, p[1]),
    'S': lambda p, n: (p[0] + n, p[1]),
    'E': lambda p, n: (p[0], p[1] + n),
    'W': lambda p, n: (p[0], p[1] - n)
}

navigate_p2 = {
    'N': lambda p_wp, n: (p_wp[0] - n, p_wp[1]),
    'S': lambda p_wp, n: (p_wp[0] + n, p_wp[1]),
    'E': lambda p_wp, n: (p_wp[0], p_wp[1] + n),
    'W': lambda p_wp, n: (p_wp[0], p_wp[1] - n),
    'L': lambda p_wp, n: (-p_wp[1], p_wp[0]),
    'R': lambda p_wp, n: (p_wp[1], -p_wp[0])
}

def dist(p):
    return abs(p[0]) + abs(p[1])

def solve_part_1(instructions):
    p = (0, 0)
    d = 90
    for direction, n in instructions:
        if direction is 'L':
            d = (d - n) % 360
        elif direction is 'R':
            d = (d + n) % 360
        elif direction is 'F':
            p = navigate[dd[d]](p, n)
        else:
            p = navigate[direction](p, n)
    return dist(p)    


def solve_part_2(instructions):
    p_wp = (-1, 10)
    p = (0, 0)
    for direction, n in instructions:
        if direction is 'F':
            p = (p[0] + p_wp[0]* n, p[1] + p_wp[1] * n)
        else:
            p_wp = navigate_p2[direction](p_wp, n)
            if direction in 'LR':
                for _ in range((n // 90)- 1):
                    p_wp = navigate_p2[direction](p_wp, n)
    return dist(p)


def main():
    instructions = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            i, n = line[0], int(line[1:])
            instructions.append((i, n))
    sol1 = solve_part_1(instructions)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(instructions)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
