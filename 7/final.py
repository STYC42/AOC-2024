from tqdm import tqdm

def read_file(file):
    with open(file) as f:
        return f.readlines()
   
def possible(resultat, nombres):
    for i in range(2**(len(nombres)-1)):
        s = nombres[0]
        for j in range(len(nombres)-1):
            if i & 2**j:
                s += nombres[j+1]
            else:
                s *= nombres[j+1]
        if s == resultat:
            return True
    return False

def possible2(resultat, nombres):
    for i in range(3**len(nombres)-1):
        s = nombres[0]
        for j in range(len(nombres)-1):
            if i % 3 == 0:
                s += nombres[j+1]
            elif i % 3 == 1:
                s *= nombres[j+1]
            else:
                s = int(str(s) + str(nombres[j+1]))
            i //= 3
        if s == resultat:
            return True
   
def part1(l):
    count = 0
    for line in l:
        s, c = line.split(":")
        c = list(map(int, c.split()))
        if possible(int(s), c):
            count += int(s)
    return count
        
def part2(l):
    count = 0
    for line in tqdm(l, leave=False):
        s, c = line.split(":")
        c = list(map(int, c.split()))
        if possible2(int(s), c):
            count += int(s)
    return count

if __name__ == "__main__":
    l = read_file("7/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))