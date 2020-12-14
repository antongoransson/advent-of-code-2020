def solve_part_1(ferry_id, buses):
    print(ferry_id //buses[0]*buses[0])
    m = 9999999999
    best_bus = None
    for bus_id in buses:
        new_m = (ferry_id //bus_id + 1) * bus_id
        if new_m < m:
            m = new_m
            best_bus = bus_id
    return (m - ferry_id) * best_bus
    return min([(ferry_id //bus_id + 1) * bus_id for bus_id in buses])

def solve_part_2(buses):
    step = buses[0][1]
    n = 0
    seen = set([buses[0][1]])
    while True:
        n += step
        for t, bus_id in buses:
            if (n + t) % bus_id == 0 and bus_id not in seen:
                seen.add(bus_id)
                step *= bus_id
        if all([(n + t) % bus_id == 0 for t, bus_id in buses]):
            return n


def main():
    buses = []
    with open('input.txt') as f:
        ferry_id = int(f.readline().strip())
        line = f.readline().strip()
        for t, bus in enumerate(line.split(',')):
            if bus != 'x':
                buses.append((t, int(bus)))
    buses_p1 = [b[1] for b in buses]
    sol1 = solve_part_1(ferry_id, buses_p1)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(buses)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
