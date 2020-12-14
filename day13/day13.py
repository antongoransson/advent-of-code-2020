def solve_part_1(ferry_id, buses):
    m = 9999999999
    best_bus = -1
    for bus_id in buses:
        new_m = (ferry_id // bus_id + 1) * bus_id
        if new_m < m:
            m = new_m
            best_bus = bus_id
    return (m - ferry_id) * best_bus

def solve_part_2(buses):
    n = buses[0][1]
    step = n
    seen = set([n])
    while True:
        n += step
        for t, bus_id in buses:
            if bus_id not in seen and (n + t) % bus_id == 0:
                seen.add(bus_id)
                step *= bus_id
                if len(seen) == len(buses):
                    return n

def main():
    with open('input.txt') as f:
        ferry_id = int(f.readline().strip())
        buses = [(t, int(bus)) for t, bus in enumerate(f.read().strip().split(',')) if bus != 'x']
    buses_p1 = [b[1] for b in buses]
    sol1 = solve_part_1(ferry_id, buses_p1)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(buses)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
