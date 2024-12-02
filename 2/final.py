


MODE = 3
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
   
   
s = 0

def safe(line):
    dif = [line[i+1]-line[i] for i in range(len(line)-1)]
    return all([abs(c)<=3 for c in dif]) and \
          (all([c>0 for c in dif]) or all([c<0 for c in dif]))
    
def part1(line):
    return safe(line)
        
def part2(line):
    global s
    if safe(line):
        return True
    for i in range(len(line)):
        if safe(line[:i]+line[i+1:]):
            return True
    return False



if __name__ == "__main__":
    l = read_file("2/input.txt")
    s = sum([int(part1(line)) for line in l])
    print("part1 :", s)
    s = sum([int(part2(line)) for line in l])
    print("part2 :", s)