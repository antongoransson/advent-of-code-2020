from collections import defaultdict
import regex as re

def get_valid_strings(rules, rule, m):
    if 'a' in rules[rule] or 'b' in rules[rule]:
        if m and m[0] in rules[rule]:
            return set([1])
        return set()
    all_matches = set()
    for opts in rules[rule]:
        sub_matches = set([0])
        for r in opts:
            new_sub_matches = set()
            for sub_match in sub_matches:
                new_sub_matches |= {sub_match + q for q in get_valid_strings(rules, r, m[sub_match:])}
            sub_matches = new_sub_matches
        all_matches |= sub_matches
    return all_matches

def solve_part_1(rules, messages):
    return len([m for m in messages if len(m) in get_valid_strings(rules, '0', m)])

# Took some inspiration from https://www.reddit.com/r/adventofcode/comments/kg1mro/2020_day_19_solutions/ggcs2a0/?context=8&depth=9 since my first solution ran out of memory trying to save all possible rule strings
def solve_part_2(rules, messages):
    n = 10
    for r in rules:
        if r == '8':
            rules[r] = [tuple(rules[r][0] * i) for i in range(1, n)]
        if r == '11':
            rules[r] = [tuple([rules[r][0][0]] * i +  [rules[r][0][1]] * i)  for i in range(1, n)]
    return len([m for m in messages if len(m) in get_valid_strings(rules, '0', m)])

def main():
    rules = defaultdict(list)
    with open('input.txt') as f:
        r, messages = f.read().split('\n\n')
        messages = [m.strip() for m in messages.split('\n')]
        for line in r.split('\n'):
            rule_n, matches = line.split(': ')
            a = matches.split(' | ')
            for b in a:
                ints = re.findall(r'\d+', b)
                if len(ints) == 0:
                    rules[rule_n].append('a' if 'a' in matches else 'b')
                else:
                    rules[rule_n].append(tuple(ints))
    sol1 = solve_part_1(rules, messages)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(rules, messages)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
