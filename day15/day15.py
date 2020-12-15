from collections import defaultdict


def solve_problem(numbers, x):
    last_index = defaultdict(lambda: -1)
    for i, n in enumerate(numbers[:-1]):
        last_index[n] = i
    n = numbers[-1]
    for i in range(len(numbers), x):
        l_i = last_index[n]
        last_index[n] = i - 1
        if l_i != -1:
            n = i - 1 - l_i
        else:
            n = 0
    return n

def solve_part_1(numbers):
    return solve_problem(numbers, 2020)
    
def solve_part_2(numbers):
    return solve_problem(numbers, 30000000)


def main():
    numbers = [6, 3, 15, 13, 1, 0]
    sol1 = solve_part_1(numbers)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(numbers)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
