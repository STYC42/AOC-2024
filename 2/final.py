


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
    if all([dif[i]>=0 for i in range(len(dif))]):
        for c in dif:
            if not 0<c<=3:
                return False
        return True
    if all([dif[i]<=0 for i in range(len(dif))]):
        for c in dif:
            if not 0>c>=-3:
                return False
        return True
    
def part1(line):
    global s
    if safe(line):
        s+=1
        
def part2(line):
    global s
    if safe(line):
        s+= 1
        return
    for i in range(len(line)):
        if safe(line[:i]+line[i+1:]):
            s+= 1
            return



if __name__ == "__main__":
    l = read_file("2/input.txt")
    for line in l:
        part1(line)
    print("part1 :", s)
    s=0
    for line in l:
        part2(line)
    print("part2 :", s)