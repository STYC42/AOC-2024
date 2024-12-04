def read_file(file):
    with open(file, 'r') as file:
        return [line.strip() for line in file]
    
def search(ch):
    return ch.count("XMAS") + ch.count("SAMX")

def part1(l):
    s = 0
    for line in l:
        s += search(line)
    for i in range(len(l[0])):
        ch = ''.join([l[j][i] for j in range(len(l))])
        s += search(ch)
    for i in range(-len(l)+1, len(l)):
        if i <= 0:
            ch = ''.join([l[-j-i][j] for j in range(len(l)) if len(l) > -j-i >= 0])
        else:
            ch = ''.join([l[len(l)-j-1][i+j] for j in range(len(l)) if len(l) > i+j >= 0])
        s += search(ch)
    for i in range(-len(l)+1, len(l[0])):
        if i < 0:
            ch = ''.join([l[-i+j][j] for j in range(len(l)) if len(l) > -i+j >= 0])
        else:
            ch = ''.join([l[j][i+j] for j in range(len(l)) if len(l) > i+j >= 0])
        s += search(ch)
    return s

def part2(l):
    s = 0
    for i in range(1, len(l)-1):
        for j in range(1, len(l)-1):
            if l[i][j] == "A":
                if {l[i-1][j-1], l[i+1][j+1]} & {l[i+1][j-1], l[i-1][j+1]} == {'S', 'M'}:
                        s += 1
    return s


if __name__ == "__main__":
    l = read_file("4/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))