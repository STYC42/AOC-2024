def read_file(file_name):
    with open(file_name, 'r') as file:
        l = [tuple(map(int, line.strip().split())) for line in file]
    return [list(x) for x in zip(*l)]
            
def part1(l, r):
    l.sort()
    r.sort()
    return sum(abs(a-b) for a, b in zip(l, r))

def part2(l, r):
    from collections import Counter
    s = 0
    c = Counter(l)
    d = Counter(r)
    return sum(k*c[k]*d[k] for k in c)

if __name__ == "__main__":
    a, b = read_file("1/input.txt")
    print("part1:", part1(a, b))
    print("part2:", part2(a, b))
    