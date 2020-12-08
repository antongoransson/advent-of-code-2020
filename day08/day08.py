class Program:

    def __init__(self, instructions):
        self.i = 0
        self.a = 0
        self.instructions = instructions
        self.ops = {
            'acc' : self.acc,
            'jmp' : self.jmp,
            'nop' : self.nop
        }
    
    def run(self):
        o, n = self.instructions[self.i]
        self.ops[o](n)
        return self.i

    def acc(self, n):
        self.a += n
        self.i += 1

    def jmp(self, n):
        self.i += n

    def nop(self, n):
        self.i += 1

    
def run_program(instructions):
    ran = set()
    i = 0
    p = Program(instructions)
    while i < len(instructions):
        ran.add(i)
        i = p.run()
        # Caught in loop
        if i in ran:
            return p.a, False
    # Finished the program
    return p.a, True

def solve_part_1(instructions):
    return run_program(instructions)[0]    


def solve_part_2(instructions):
    switch = {'jmp': 'nop', 'nop': 'jmp'}
    for i in range(len(instructions)):
        if instructions[i][0] in switch:
            instructions[i][0] = switch[instructions[i][0]]
            a, finished = run_program(instructions)
            instructions[i][0] = switch[instructions[i][0]]
            if finished:
                return a
            

def main():
    instructions = []
    with open('input.txt') as f:
        for line in f:
            i, n = line.strip().split(' ')
            instructions.append([i, int(n)])
    sol1 = solve_part_1(instructions)
    print('Part 1: {}'.format(sol1))
    
    sol2 = solve_part_2(instructions)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
