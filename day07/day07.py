from collections import defaultdict

def get_path(bag_rules, bag):
    if not bag_rules[bag]:
        return False
    if 'shiny gold' in bag_rules[bag]:
        return True
    return any([get_path(bag_rules, b) for b in bag_rules[bag]])

def get_n_bags(bag_rules, bag):
    if not bag_rules[bag]:
        return 0
    bags = bag_rules[bag]
    return sum([bags[b] + bags[b] * get_n_bags(bag_rules, b) for b in bags])

def solve_part_1(bag_rules):
    return sum([get_path(bag_rules, b) for b in bag_rules])

def solve_part_2(bag_rules):
    return get_n_bags(bag_rules, 'shiny gold')

def main():
    bag_rules = defaultdict(dict)
    with open('input.txt') as f:
        for line in f:
            line = line.strip().split(' contain ')
            b = line[0][:-5]
            bags_in_bag = line[1].split(', ')
            for bag in bags_in_bag:
                a = bag.split(' ')
                if a[0] == 'no':
                    bag_rules[b] = 0
                else:
                    s = a[1] + ' ' + a[2]
                    bag_rules[b][s] = int(a[0])
    sol1 = solve_part_1(bag_rules)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(bag_rules)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
