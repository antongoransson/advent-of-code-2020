import regex as re

def play(d1, d2, prev_plays, p2 = False):
    prev_d = set()
    while d1 and d2:
        round_winner = None
        t = (tuple(d1), tuple(d2))
        if t in prev_d and p2:
            return 'P1'
        prev_d.add(t)
        if t in prev_plays:
            return prev_plays[t]
        c1 = d1.pop(0)
        c2 = d2.pop(0)
        if len(d1) >= c1 and len(d2) >= c2 and p2:
            round_winner = play(d1[:c1], d2[:c2], prev_plays, p2)
        else:
            round_winner = 'P1' if c1 > c2 else 'P2'
        if round_winner == 'P1':
            d1.extend([c1, c2])
        else:
            d2.extend([c2, c1])
        prev_plays[t] = round_winner
    return 'P1' if d1 else 'P2'

def solve_part_1(d1, d2):
    prev_plays = {}
    w = d1 if play(d1, d2, prev_plays) else 2
    return sum((i + 1) * c for i, c in enumerate(reversed(w))) 

def solve_part_2(d1, d2):
    prev_plays = {}
    w = d1 if play(d1, d2, prev_plays, True) else d2
    return sum((i + 1) * c for i, c in enumerate(reversed(w))) 

def get_ints(s):
   return list(map(int, re.findall(r'-?\d+', s)))

def main():
    with open('input.txt') as f:
        s = f.read().split('\n\n')
        d1 = (get_ints(s[0][9:]))
        d2 = (get_ints(s[1][9:]))
    sol1 = solve_part_1(d1.copy(), d2.copy())
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(d1, d2)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
