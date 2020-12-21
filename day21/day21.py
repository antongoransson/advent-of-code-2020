from collections import Counter
from itertools import combinations
import regex as re

def reduce_allergens(allergens):
    for _ in range(len(allergens)):
        for a1, a2 in combinations(allergens, 2):
            if len(allergens[a1]) == 1:
                x, = allergens[a1]
                allergens[a2].discard(x)
            if len(allergens[a2]) == 1:
                x, = allergens[a2]
                allergens[a1].discard(x)
    return allergens

    
def solve_part_1(allergens, ingredient_count):
    allergen_ingredienst = set(i for i_set in reduce_allergens(allergens).values() for i in i_set )
    return sum(i_count for i, i_count in ingredient_count.items() if i not in allergen_ingredienst)

def solve_part_2(allergens, ingredients):
    allergens = reduce_allergens(allergens)
    return ','.join([i for a in sorted(allergens.keys()) for i in allergens[a]])


def main():
    allergen_ingredients = {}
    ingredient_count = Counter()
    with open('input.txt') as f:
        for line in f:
            line = re.match(r'([a-z ]+) \(contains ([a-z]+[, a-z]*)\)', line.strip())
            a_ingredients = set(line.group(1).split(' '))
            allergens = set(line.group(2).replace(',', '').split(' '))
            ingredient_count.update(a_ingredients)
            for i in allergens:
                if i in allergen_ingredients:
                    allergen_ingredients[i] &= a_ingredients
                else:
                    allergen_ingredients[i] = set(a_ingredients)
    sol1 = solve_part_1(allergen_ingredients, ingredient_count)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(allergen_ingredients, ingredient_count)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
