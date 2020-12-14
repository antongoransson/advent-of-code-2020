import regex as re

def get_op(instruction):
    if 'mask' in instruction:
        return instruction.split('= ')[1], True
    return map(int, re.findall(r'-?\d+', instruction)), False

def solve_part_1(program):
    mem = {}
    is_mask = None
    mask = None
    for instruction in program:
        op, is_mask = get_op(instruction)
        if is_mask:
            mask = op
        else:
            i, v = op
            v_bin = [s for s in "{0:b}".format(v).zfill(len(mask))]
            for j in range(len(mask)):
                if mask[j] != 'X':
                    v_bin[j] = mask[j]
            mem[i] = int(''.join(v_bin),2) 
    return sum([v for v in mem.values()])

def solve_part_2(program):
    mem = {}
    is_mask = None
    mask = None
    for instruction in program:
        op, is_mask = get_op(instruction)
        if is_mask:
            mask = op
        else:
            i, v = op
            values = [[s for s in "{0:b}".format(i).zfill(len(mask))]]
            for j in range(len(mask)):
                if mask[j] == '1':
                    for v_bin in values:
                        v_bin[j] = mask[j]
                elif mask[j] == 'X':
                    temp = []
                    for v_bin in values:
                       c = [x for x in v_bin]
                       v_bin[j] = '1'
                       c[j] = '0'
                       temp.append(c)
                    values.extend(temp)
            for v_bin in values:
                mem[int(''.join(v_bin),2)] = v
    return sum([v for v in mem.values()])


def main():
    mem = {}
    with open('input.txt') as f:
        program = [line.strip() for line in f]
    sol1 = solve_part_1(program)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(program)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
