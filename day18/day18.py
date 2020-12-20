def is_int(c):
    try:
        int(c)
        return True
    except:
        return False

def evaluate(expr, acc = 0):
    i = len(expr) - 1
    x = None
    while i >= 0:
        if expr[i] is '+':
            return x + evaluate(expr[: i])
        elif expr[i] is '*':
            return x * evaluate(expr[: i])
        elif expr[i] is ')':
            sub_expr = ''
            n_right = 1
            while True:
                i -= 1
                if expr[i] is ')':
                    n_right += 1
                elif expr[i] is '(':
                    n_right -= 1
                    if n_right == 0:
                        break
                sub_expr = expr[i] + sub_expr
            x = evaluate(sub_expr)
        else:
            s = ''
            while i >= 0 and is_int(expr[i]):
                s += expr[i]
                i -= 1
            i += 1
            x = int(s)
        i -= 1 
    return x

# Might be the stupidest shit ever, but it works https://en.wikipedia.org/wiki/Operator-precedence_parser#Alternative_methods
def parse(expr):
    new_expr = []
    for c in reversed(expr):
        new_expr.append(c)
        if c is '+':
            new_expr.insert(len(new_expr) - 1, '(')
            new_expr.append(')')
        if c is '*':
            new_expr.insert(len(new_expr) - 1, '(')
            new_expr.insert(len(new_expr) - 1, '(')
            new_expr.append(')')
            new_expr.append(')')
        if c in ')(':
            new_expr.extend(c * 2)
    return ['(','('] + list(reversed(new_expr)) + [')', ')']

def solve_part_1(expressions):
    return sum([evaluate(e) for e in expressions])


def solve_part_2(expressions):
    return sum([evaluate(parse(e)) for e in expressions])


def main():
    with open('input.txt') as f:
        expressions = [line.strip().replace(' ', '') for line in f]
    sol1 = solve_part_1(expressions)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(expressions)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
