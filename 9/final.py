from tqdm import tqdm

def read_file(file):
    with open(file, 'r') as file:
        l = [line.strip() for line in file]
    return l
   
def part1(l):
    i = 0
    j = len(l)-1
    c = 0
    d = 0
    s = 0
    k = 0
    while i < j:
        if c >= int(l[i]):
            c = 0
            i += 1
        elif d >= int(l[j]) or j%2:
            d = 0
            j -= 1
        elif i%2:
            c += 1
            d += 1
            s += (j//2)*k
            k += 1
        else:
            c += 1
            s += (i//2)*k
            k += 1
    if i == j:
        c = c+d
        while c < int(l[i]):
            c += 1
            s += (i//2)*k
            k += 1
    return s
        
def part2(l):
    s = 0
    k = 0
    d = 0
    depl = [False]*len(l)
    for i, c in tqdm(list(enumerate(l)), leave=False):
        if i%2:
            d = int(c)
            for j in range(len(l)-1, i, -1):
                if not depl[j] and j%2==0 and int(l[j]) <= d:
                        for _ in range(int(l[j])):
                            s += (j//2)*k
                            k += 1
                        depl[j] = True
                        d -= int(l[j])
            k += d
        else:
            if not depl[i]:
                for _ in range(int(c)):
                    s += (i//2)*k
                    k += 1
                depl[i] = True
            else:
                k += int(c)
    return s



if __name__ == "__main__":
    l = read_file("9/input.txt")[0]
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))