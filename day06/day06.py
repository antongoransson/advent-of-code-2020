from functools import reduce

def solve_part_1(answers):
    return sum([len(set([c for  c in ''.join(a)])) for a in answers])


def solve_part_2(answers):
    return sum([len(reduce(set.intersection, [set([c for c in x]) for x in a])) for a in answers])


def main():
    with open('input.txt') as f:
        a = list(map(lambda x: x.split('\n'), f.read().split('\n\n')))
    sol1 = solve_part_1(a)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(a)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
