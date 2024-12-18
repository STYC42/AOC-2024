
import re

def read_file(file):
    with open(file, 'r') as file:
        return file.readlines()
        
def decrypt(l):
    pattern = r"(\d+),(\d+)"
    return [tuple(map(int, re.match(pattern, line).groups())) for line in l]

def correct(l, i):
    obst = l[:i]
    pile = [(0, 0)]
    visited = set()

    while pile:
        x, y = pile.pop()

        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if (x+dx, y+dy) in obst:
                continue
            if 0<=x+dx<=70 and 0<=y+dy<=70:
                if (x+dx, y+dy) == (70, 70):
                    return True
                pile.append((x+dx, y+dy))
    return False
   
def part1(l):
    l = decrypt(l)
    obst = l[:1024]
    
    pile = [(0, 0, 0)]
    visited = set()

    while pile:
        x, y, lev = min(pile, key=lambda x: x[2])
        pile.remove((x, y, lev))

        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if (x+dx, y+dy) in obst:
                continue
            if 0<=x+dx<=70 and 0<=y+dy<=70:
                if (x+dx, y+dy) == (70, 70):
                    return lev+1
                pile.append((x+dx, y+dy, lev+1))

        
def part2(l):
    l = decrypt(l)

    i = 1024
    j = len(l)
    m = (i + j) // 2
    while i < j-1:
        corr = correct(l, m+1)
        if corr:
            i = m
        else:
            j = m
        m = (i+j) // 2

    return ','.join(map(str, l[i+1]))


if __name__ == "__main__":
    l = read_file("18/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))