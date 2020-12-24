from collections import defaultdict, Counter

d = {
    'e' : (1, -1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
    'w': (-1, 1, 0),
    'nw': (0, 1, -1),
    'ne': (1, 0, -1)
}

def get_black_tiles(tiles):
    flipped_tiles = defaultdict(lambda: False)
    for tile in tiles:
        x, y, z = 0, 0 ,0
        for c in tile:
            dx, dy, dz = d[c] 
            x, y, z = dx + x, dy + y, dz + z
        flipped_tiles[(x, y, z)] = not(flipped_tiles[(x, y, z)])
    return set(p for p, v in flipped_tiles.items() if v)

def get_neighbours(pos):
    x, y, z = pos
    return [(x + dx, y + dy, z + dz) for dx, dy, dz in d.values()]

def solve_part_1(tiles):
    return len(get_black_tiles(tiles))



def solve_part_2(tiles):
    ts = get_black_tiles(tiles)
    for _ in range(100):
        c = Counter(n for t in ts for n in get_neighbours(t))
        ts = set(t for t,n in c.items() if t in ts and 1 <= n <= 2 or t not in ts and n == 2)
    return len(ts)

def main():
    tiles = []
    with open('input.txt') as f:
        for j, line in enumerate(f):
            line = line.strip()
            i = 0
            tiles.append([])
            while i < len(line):
                if line[i] in ['w', 'e']:
                    tiles[j].append(line[i])
                    i += 1
                else:
                    tiles[j].append(line[i] + line[i + 1])
                    i += 2
    sol1 = solve_part_1(tiles)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(tiles)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
