


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



def part1(l):
    s = 0
    for line in l:
        s += line.count("XMAS")
        s += line.count("SAMX")
    for i in range(len(l[0])):
        ch = ''.join([l[j][i] for j in range(len(l))])
        s += ch.count("XMAS")
        s += ch.count("SAMX")
    for i in range(-len(l)+1, len(l)):
        if i <= 0:
            ch = ''.join([l[-j-i][j] for j in range(len(l)) if len(l) > -j-i >= 0])
        else:
            ch = ''.join([l[len(l)-j-1][i+j] for j in range(len(l)) if len(l) > i+j >= 0])
        s += ch.count("XMAS")
        s += ch.count("SAMX")
    for i in range(-len(l)+1, len(l[0])):
        if i < 0:
            ch = ''.join([l[-i+j][j] for j in range(len(l)) if len(l) > -i+j >= 0])
        else:
            ch = ''.join([l[j][i+j] for j in range(len(l)) if len(l) > i+j >= 0])
        s += ch.count("XMAS")
        s += ch.count("SAMX")
        
    print(s)

def part2(l):
    s = 0
    for i in range(1, len(l)-1):
        for j in range(1, len(l)-1):
            if l[i][j] == "A":
                if l[i-1][j-1] == "M" and l[i+1][j+1] == "S" or l[i-1][j-1] == 'S' and l[i+1][j+1] == 'M':
                    if l[i+1][j-1] == "M" and l[i-1][j+1] == 'S' or l[i+1][j-1] == 'S' and l[i-1][j+1] == 'M':
                        s += 1
    print(s)


if __name__ == "__main__":
    l = read_file("4/input.txt")
    part2(l)