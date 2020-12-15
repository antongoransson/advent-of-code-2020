from collections import defaultdict, Counter
import regex as re

def solve_part_1(adapters):
    diffs = Counter([adapters[i + 1] - adapters[i] for i in range(len(adapters)- 1)])
    return diffs[1] * diffs[3]

def solve_part_2(adapters):
    n_paths = defaultdict(int)
    n_paths[0] = 1
    for i in range(1, len(adapters)):
        j = i
        while j > 0 and adapters[i] - adapters[j - 1] <= 3:
            n_paths[adapters[i]] += n_paths[adapters[j - 1]]
            j -= 1
    return n_paths[adapters[-1]]

def main():
    with open('input.txt') as f:
        adapters = [0] + sorted(list(map(int, re.findall(r'-?\d+', f.read()))))
        adapters.append(adapters[-1] + 3)
    sol1 = solve_part_1(adapters)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(adapters)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
