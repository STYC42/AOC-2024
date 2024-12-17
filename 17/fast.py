import re
from tqdm import tqdm


MODE = 0
NUMBER = 0

def read_file(file):
    with open(file, 'r') as file:
        if MODE == 0:
            # return list of strings
            return [line.strip() for line in file]
        elif MODE == 1:
            # return list of tuples of strings
            return [tuple(line.strip().split()) for line in file]
        elif MODE == 2:
            # return list of integers
            return [int(line) for line in file]
        elif MODE == 3:
            # return list of tuples of integers
            return [tuple(map(int, line.strip().split())) for line in file]
        elif MODE == 4:
            # return list of parallel lists of integers
            return [[int(line.split()[i]) for line in file] for i in range(NUMBER)]
        elif MODE == 5:
            # return list of parallel lists of strings
            return [[line.split()[i] for line in file] for i in range(NUMBER)]
        elif MODE == 6:
            #return all lines as a single string
            return file.read().strip()
        
def decrypt(l):
    pattern = r"Register\s[A-C]:\s(\d+)"

    registers = [0, 0, 0]

    registers[0] = int(re.match(pattern, l[0]).group(1))
    registers[1] = int(re.match(pattern, l[1]).group(1))
    registers[2] = int(re.match(pattern, l[2]).group(1))

    pattern = r"Program:\s(.*)"

    program = list(map(int, re.match(pattern, l[4]).group(1).split(",")))

    return registers, program

def combo(registers, value):
    if 0 <= value <= 3:
        return value
    if 4 <= value <= 6:
        return registers[value-4]
    if value == 7:
        raise Exception("Invalid value")


def run(registers, program):
    i = 0
    out = []
    while i < len(program):
        instr = program[i]
        if instr == 0: #adv
            registers[0] = registers[0] // 2**combo(registers, program[i+1])
            i += 2
        elif instr == 1: #bxl
            registers[1] = registers[1]^program[i+1]
            i += 2
        elif instr == 2: #bst
            registers[1] = combo(registers, program[i+1]) % 8
            i += 2
        elif instr == 3: #jnz
            if registers[0]:
                i = program[i+1]
            else:
                i += 2
        elif instr == 4: #bxc
            registers[1] = registers[1]^registers[2]
            i += 2
        elif instr == 5: #out
            out.append(combo(registers, program[i+1])%8)
            i += 2
        elif instr == 6: #bdv
            registers[1] = registers[0] // 2**combo(registers, program[i+1])
            i += 2
        elif instr == 7: #cdv
            registers[2] = registers[0] // 2**combo(registers, program[i+1])
            i += 2

    return out

def find(i, A, program):
    if i == -1:
        assert run([A, 0, 0], program) == program
        return A
    A *= 8
    for k in range(8):
        if run([A+k, 0, 0], program) == program[i:]:
            if (r:=find(i-1, A+k, program)) is not None:
                return r

   
def part1(l):
    registers, program = decrypt(l)
    return ','.join(map(str, run(registers, program)))
        
def part2(l):
    registers, program = decrypt(l)
    A = find(len(program)-1, 0, program)
    return A
    


if __name__ == "__main__":
    l = read_file("17/test.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))