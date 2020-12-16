from collections import defaultdict
from functools import reduce
from operator import mul
import regex as re

def get_ok_fields(value, fields):
    possible_fields = set()
    for field, ranges in fields.items():
        r1, r2 = ranges
        if r1[0] <= value <= r1[1] or r2[0] <= value <= r2[1]:
            possible_fields.add(field)
    return possible_fields


def get_ok_fields_for_ticket(ticket, fields):
    ok_fields_for_ticket = {}
    for i, value in enumerate(ticket):
            ok_fields = get_ok_fields(value, fields)
            if ok_fields:
                ok_fields_for_ticket[i] = ok_fields
            else:
                ok_fields_for_ticket = {}
                break
    return ok_fields_for_ticket

def reduce_fields(all_fields):
    while not all([len(fields) == 1 for fields in all_fields.values()]):
        for i, fields in all_fields.items():
            if len(fields) == 1:
                field, = fields
                for j in all_fields:
                    if i != j and field in all_fields[j]:
                        all_fields[j].remove(field)

def solve_part_1(fields, my_ticket, nearby_tickets):
    return sum([v for ticket in nearby_tickets for v in ticket if not get_ok_fields(v, fields)])

def solve_part_2(fields, my_ticket, nearby_tickets):
    all_fields = defaultdict(lambda: set([f for f in fields]))
    for ticket in nearby_tickets:
        ok_fields_for_ticket = get_ok_fields_for_ticket(ticket, fields)
        for i, ok_fields in ok_fields_for_ticket.items():
            all_fields[i] &= ok_fields
    reduce_fields(all_fields)
    return reduce(mul, [my_ticket[i] for i, (field, ) in all_fields.items() if 'departure' in field])
def main():
    fields = {}
    with open('input.txt') as f:
        s = f.read().split('\n\n')
        for line in s[0].split('\n'):
            line = line.strip()
            field = line.split(':')[0]
            rl1, ru1, rl2, ru2 = map(int, re.findall(r'\d+', line))
            fields[field] = [(rl1, ru1), (rl2, ru2)]
        my_ticket = list(map(int, re.findall(r'\d+', s[1])))
        nearby_tickets = [list(map(int, re.findall(r'\d+', line))) for line in s[2].split('\n')[1:]]
    sol1 = solve_part_1(fields, my_ticket, nearby_tickets)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(fields, my_ticket, nearby_tickets)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
