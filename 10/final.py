
def read_file(file):
    with open(file, 'r') as file:
        l = [line.strip() for line in file]
    return l
   
def findheads(l):
    for i, line in enumerate(l):
        for j, c in enumerate(line):
            if c == '0':
                yield (i, j)

def neighbors(l, i, j):
    for pos in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if pos[0] >= 0 and pos[0] < len(l) and pos[1] >= 0 and pos[1] < len(l[0]):
            if int(l[pos[0]][pos[1]]) == 1 + int(l[i][j]):
                yield pos

def bfs(l, i, j):
    s = []
    q = [(i, j)]
    while q:
        i, j = q.pop(0)
        for pos in neighbors(l, i, j):
            if l[pos[0]][pos[1]] == '9':
                s.append(pos)
            else:
                q.append(pos)
    return s

def part1(l):
    s = 0
    for i, j in findheads(l):
        s += len(set(bfs(l, i, j)))
    return s
        
def part2(l):
    s = 0
    for i, j in findheads(l):
        s += len(bfs(l, i, j))
    return s


if __name__ == "__main__":
    l = read_file("10/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))