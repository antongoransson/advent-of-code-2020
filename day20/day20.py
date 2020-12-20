from collections import defaultdict
from itertools import combinations
from functools import reduce
from operator import mul
import regex as re

def rotate(image):
    return [list(a) for a in zip(*image[::-1])]

def flip(image):
    return [row[::-1] for row in image]

def get_right(image):
    return ''.join([row[-1] for row in image])

def get_left(image):
    return ''.join([row[0] for row in image])

def get_top(image):
    return ''.join(image[0])

def get_bottom(image):
    return ''.join(image[-1])

def get_edges(image):
    return set([get_top(image), get_bottom(image), get_left(image),get_right(image)])

sides = {
    'T': get_top,
    'B': get_bottom,
    'L': get_left,
    'R': get_right
}
opposites = {
    'T': 'B',
    'B': 'T',
    'L': 'R',
    'R': 'L'
}

def get_all_options(image):
    all_options = []
    for _ in range(4):
        all_options.append(image)
        all_options.append(flip(image))
        image = rotate(image)
    return all_options

def get_all_edges(image):
    all_edges = set()
    for _ in range(4):
        all_edges |= get_edges(image)
        all_edges |= get_edges(flip(image))
        image = rotate(image)
    return all_edges

def get_matches(image):
    matches = defaultdict(set)
    orientations = {tile_id : get_all_edges(tiles) for tile_id, tiles in image.items()}
    for t1_id, t2_id in combinations(image, 2):
        tile1_sides = orientations[t1_id]
        tile2_sides = orientations[t2_id]
        for s1 in tile1_sides:
            if s1 in tile2_sides:
                matches[t1_id].add(t2_id)
                matches[t2_id].add(t1_id)
    return matches

def solve_part_1(image):
    return reduce(mul, [tile_id for tile_id, match in get_matches(image).items() if len(match) == 2])

def reduce_tiles(grid):
    acc = [[''] for _ in range(12 * 8)]
    for k, row in enumerate(grid):
        for i, (tile,_) in enumerate(row):
            for j, tile_row in enumerate(tile[1 : -1]):
                acc[j + 8 * k] += ''.join(tile_row[1 : -1])
    return acc

def get_base(image, c0, matches):
    for tile in get_all_options(image[c0]):
        adjacent = {}
        for adj_tile_id in matches[c0]:
            for adj_tile in get_all_options(image[adj_tile_id]):
                if sides['R'](tile) == sides['L'](adj_tile):
                    adjacent['R'] = (adj_tile, adj_tile_id)
                elif sides['B'](tile) == sides['T'](adj_tile):
                    adjacent['B'] = (adj_tile, adj_tile_id)
        if 'R' in adjacent and 'B' in adjacent:
            matches[adjacent['R'][1]].remove(c0)
            matches[adjacent['B'][1]].remove(c0)
            return tile, adjacent

def find(tile, tile_id, image, grid, matches, d):
    for adj_tile_id in matches[tile_id]:
        for adj_tile in get_all_options(image[adj_tile_id]):
            if sides[d](tile) == sides[opposites[d]](adj_tile):
                return (adj_tile, adj_tile_id)

def find_right(tile, tile_id, image, grid, matches):
    return find(tile, tile_id, image, grid, matches, 'R')
    
def find_bottom(tile, tile_id, image, grid, matches):
    return find(tile, tile_id, image, grid, matches, 'B')
    
def found_sea_monsters(image, sea_monster):
    found = False
    for r in range(len(image) - 2):
        for c in range(len(image) - 19):
            if all(image[r + dr][c + dc] == '#' for dr, dc in sea_monster):
                found = True
                for dr, dc in sea_monster:
                    image[r + dr][c + dc] = '.'
    return found

def solve_part_2(image):
    matches = get_matches(image)
    corners = [tile_id for tile_id, match in matches.items() if len(match) == 2]
    # Pick a corner to start in and make sure we start building to the bottom and right
    c0 = corners[0]
    c0_state, adjacent = get_base(image, c0, matches) 
    grid = [[(c0_state, c0), adjacent['R']], [adjacent['B']]]
    row = 0
    col = 1
    n = 12
    while True:
        if (col + 1) % (n) == 0:
            col, row = 0, row + 1
            if row == n:
                break
            grid.append([])
            if row < n - 1:
                tile, tile_id = grid[row][col]  
                adj_tile, adj_tile_id = find_bottom(tile, tile_id, image, grid, matches) 
                grid[row + 1].append((adj_tile, adj_tile_id))
        else:
            tile, tile_id = grid[row][col]
            adj_tile, adj_tile_id = find_right(tile, tile_id, image, grid, matches)
            grid[row].append((adj_tile, adj_tile_id))
            col += 1
        matches[tile_id].discard(adj_tile_id)
        matches[adj_tile_id].discard(tile_id)

    reduced_image = reduce_tiles(grid)
    sea_monster = [
        (0, 18), 
        (1, 0), (1,5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
        (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)
    ]
    for image_opt in get_all_options(reduced_image):
        if found_sea_monsters(image_opt, sea_monster):
            return sum(row.count('#') for row in image_opt)

def main():
    image = {}
    with open('input.txt') as f:
        for tile in f.read().split('\n\n'):
            tile_id, = map(int, re.findall(r'-?\d+', tile))
            image[tile_id] = []
            for r, row in enumerate(tile.split('\n')[1:]):
                image[tile_id].append([col for col in row.strip()])
    sol1 = solve_part_1(image)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(image)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
