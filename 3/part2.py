


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
   
import re
   
def part1(txt):
    pat = r"mul\((-?\d+),\s*(-?\d+)\)"
    r = re.findall(pat, txt)
    s = 0
    for a, b in r:
        a = int(a)
        b = int(b)
        s += a*b
    return s
      
def main(txt):
    s = txt.split("do()")
    f = []
    for a in s:
        f.append(a.split("don't")[0])
    s = 0
    for a in f:
        s += part1(a)
    return s


if __name__ == "__main__":
    l = read_file("3/input.txt")
    acc = ""
    for line in l:
        acc = acc + line
    print(main(acc))