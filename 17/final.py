import re


def read_file(file):
    with open(file, 'r') as file:
        return file.readlines()
        
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
    A, B, C = registers
    out = []
    while i < len(program):
        instr = program[i]
        oper = program[i+1]
        match instr:
            case 0:
                A = A // 2**combo((A, B, C), oper)
                i += 2
            case 1: 
                B = B^oper
                i += 2
            case 2:
                B = combo((A, B, C), oper) % 8
                i += 2
            case 3:
                if A: i = oper
                else: i += 2
            case 4:
                B = B^C
                i += 2
            case 5:
                out.append(combo((A, B, C), oper) % 8)
                i += 2
            case 6:
                B = A // 2**combo((A, B, C), oper)
                i += 2
            case 7:
                C = A // 2**combo((A, B, C), oper)
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
    l = read_file("17/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))