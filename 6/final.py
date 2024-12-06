def read(file):
    with open(file) as f:
        return [line.strip() for line in f]
    
def pos_guard(l):
    for i, line in enumerate(l):
        for j, c in enumerate(line):
            if c in "^<>v":
                return (i, j), "^>v<".index(c)
    
def access(l, npos):
    x, y = npos
    return 0 <= x < len(l[0]) and 0 <= y < len(l) 

def next_pos(l, g):
    pos, dir = g
    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
    npos = tuple(map(sum, zip(pos, dirs[dir])))
    if not access(l, npos):
        return None
    elif l[npos[0]][npos[1]] != "#":
        return npos, dir
    else:
        return pos, (dir+1)%4
    
def walk(l, g):
    while g is not None:
        yield g
        g = next_pos(l, g)
    
def positions(l, g):
    w = walk(l, g)
    return list({pos for pos, dir in w})

def loop(l, g):
    w = walk(l, g)
    spos = set()
    for g in w:
        if g in spos:
            return True
        spos.add(g)
    return False

def part1(l):
    g = pos_guard(l)
    posit = positions(l, g)
    return len(posit)

def part2(l):
    from tqdm import tqdm

    g = pos_guard(l)
    posit = positions(l, g)

    count = 0

    for cpos in tqdm(posit, leave=False):
        i, j = cpos
        tmp = l[i]
        l[i] = l[i][:j] + "#" + l[i][j+1:]
        if loop(l, g):
            count += 1
        l[i] = tmp

    return count


if __name__ == "__main__":
    l = read("6/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))