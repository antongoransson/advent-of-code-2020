from collections import defaultdict
import regex as re


def solve_part_1(passwords):
    return len([1 for item in passwords if item['n_max'] >= item['pw'].count(item['c']) >= item['n_min']])


def solve_part_2(passwords):
     return len([1 for item in passwords if ((item['pw'][item['n_max']- 1] == item['c']) ^ (item['pw'][item['n_min'] - 1] == item['c']))])


def main():
    passwords = []
    with open('input.txt') as f:
        for line in f:
            n_min, n_max = list(map(int, re.findall(r'\d+', line)))
            c, pw = line.split(': ')
            passwords.append({'n_min': n_min, 'n_max': n_max, 'c': c[-1], 'pw': pw.strip()})
    sol1 = solve_part_1(passwords)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(passwords)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
