
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
    START = (len(l)-2, 1)
    GOAL = (1, len(l[0])-2)
    
    q = []
    dist = {}
    prev = {}
    for i in range(len(l)):
        for j in range(len(l[0])):
            for dir in range(4):
                dist[(i, j, dir)] = float('inf')
                prev[(i, j, dir)] = None
    dist[(*START, 1)] = 0
    q.append((*START, 1))

    while q:
        i, j, dir = min(q, key=lambda x: dist[x])
        q.remove((i, j, dir))

        if (i, j) == GOAL:
            print("REACHED GOAL")
            break
        
        for new_dir in range(4):
            I, J = i, j
            if (new_dir-dir) % 4 == 2:
                continue
            if new_dir == dir:
                alt = dist[(i, j, dir)] + 1
                if dir == 0:
                    I -= 1
                elif dir == 1:
                    J += 1
                elif dir == 2:
                    I += 1
                elif dir == 3:
                    J -= 1
                if 0 <= I < len(l) and 0 <= J < len(l[0]) and l[I][J] != '#' and alt < dist[(I, J, dir)]: 
                    dist[(I, J, dir)] = alt
                    prev[(I, J, dir)] = (i, j, dir)
                    q.append((I, J, dir))
            else:
                alt = dist[(i, j, dir)] + 1000
                if alt < dist[(i, j, new_dir)]:
                    dist[(i, j, new_dir)] = alt
                    prev[(i, j, new_dir)] = (i, j, dir)
                    q.append((i, j, new_dir))

    return min(dist[(*GOAL, 0)], dist[(*GOAL, 1)], dist[(*GOAL, 2)], dist[(*GOAL, 3)])


        
def part2(l):
    START = (len(l)-2, 1)
    GOAL = (1, len(l[0])-2)
    
    q = []
    dist = {}
    prev = {}
    for i in range(len(l)):
        for j in range(len(l[0])):
            for dir in range(4):
                dist[(i, j, dir)] = float('inf')
                prev[(i, j, dir)] = []
    dist[(*START, 1)] = 0
    q.append((*START, 1))

    while q:
        i, j, dir = min(q, key=lambda x: dist[x])
        q.remove((i, j, dir))

        if (i, j) == GOAL:
            print("REACHED GOAL")
            break
        
        for new_dir in range(4):
            I, J = i, j
            if (new_dir-dir) % 4 == 2:
                continue
            if new_dir == dir:
                alt = dist[(i, j, dir)] + 1
                if dir == 0:
                    I -= 1
                elif dir == 1:
                    J += 1
                elif dir == 2:
                    I += 1
                elif dir == 3:
                    J -= 1
                if 0 <= I < len(l) and 0 <= J < len(l[0]) and l[I][J] != '#' and alt < dist[(I, J, dir)]: 
                    dist[(I, J, dir)] = alt
                    prev[(I, J, dir)] = [(i, j, dir)]
                    q.append((I, J, dir))
                elif 0 <= I < len(l) and 0 <= J < len(l[0]) and l[I][J] != '#' and alt == dist[(I, J, dir)]:
                    prev[(I, J, dir)].append((i, j, dir))
            else:
                alt = dist[(i, j, dir)] + 1000
                if alt == dist[(i, j, new_dir)]:
                    prev[(i, j, new_dir)].append((i, j, dir))
                if alt < dist[(i, j, new_dir)]:
                    dist[(i, j, new_dir)] = alt
                    prev[(i, j, new_dir)] = [(i, j, dir)]
                    q.append((i, j, new_dir))

    m = float('inf')
    val = 0
    for i in range(4):
        if dist[(*GOAL, i)] < m:
            m = dist[(*GOAL, i)]
            s = set()
            visited = set()
            pile = [(GOAL[0], GOAL[1], i)]
            while pile:
                I, J, DIR = pile.pop()
                s.add((I, J))
                visited.add((I, J, DIR))
                for p in prev[(I, J, DIR)]:
                    if p not in visited:
                        pile.append(p)
            val = len(s)
        elif dist[(*GOAL, i)] == m:
            s = set()
            visited = set()
            pile = [(GOAL[0], GOAL[1], i)]
            while pile:
                I, J, DIR = pile.pop()
                s.add((I, J))
                visited.add((I, J, DIR))
                for p in prev[(I, J, DIR)]:
                    if p not in visited:
                        pile.append(p)
            val += len(s)
    return val
                



if __name__ == "__main__":
    l = read_file("16/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))