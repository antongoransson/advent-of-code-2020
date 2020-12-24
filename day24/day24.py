from collections import defaultdict, Counter
import regex as re

d = {
    'e' : (1, -1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
    'w': (-1, 1, 0),
    'nw': (0, 1, -1),
    'ne': (1, 0, -1)
}

def get_black_tiles(tiles):
    flipped_tiles = Counter(tuple(map(sum, zip(*[d[c] for c in t]))) for t in tiles)
    return set(p for p, v in flipped_tiles.items() if v % 2 == 1)

def get_neighbours(pos):
    x, y, z = pos
    return [(x + dx, y + dy, z + dz) for dx, dy, dz in d.values()]

# See https://stackoverflow.com/questions/1838656/how-do-i-represent-a-hextile-hex-grid-in-memory/16874550#16874550 for representing hexagons in a grid
def solve_part_1(tiles):
    return len(get_black_tiles(tiles))

def solve_part_2(tiles):
    ts = get_black_tiles(tiles)
    for _ in range(100):
        c = Counter(n for t in ts for n in get_neighbours(t))
        ts = set(t for t,n in c.items() if t in ts and 1 <= n <= 2 or t not in ts and n == 2)
    return len(ts)

def main():
    with open('input.txt') as f:
        tiles = [re.findall(r'e|w|sw|se|nw|ne', line) for line in f]
    sol1 = solve_part_1(tiles)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(tiles)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
