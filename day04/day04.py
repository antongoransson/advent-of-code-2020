import regex as re

eye_colors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
def validate_height(x):
    if 'cm' in x:
        return 150 <= int(x[:-2]) <= 193
    if 'in' in x:
        return 59 <= int(x[:-2]) <= 76
    return False

fields =  {
    'byr' : lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': validate_height,
    'hcl': lambda x: re.findall(r'#[\d|a-z][\d|a-z][\d|a-z][\d|a-z][\d|a-z][\d|a-z]', x),
    'ecl': lambda x: x in eye_colors,
    'pid': lambda x: len(re.findall(r'\d+', x)[0]) == 9
}

def solve_part_1(passports):
    return len([p for p in passports if all([f in p for f in fields])])


def solve_part_2(passports):
    return len([p for p in passports if all([f in p and validator(p[f]) for f, validator in fields.items()])])


def main():
    passports = []
    with open('input.txt') as f:
        for line in f.read().split('\n\n'):
            a = line.replace('\n', ' ')
            passports.append({k.split(':')[0] : k.split(':')[1] for k in pairs })
    sol1 = solve_part_1(passports)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(passports)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
