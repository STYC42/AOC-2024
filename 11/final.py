from functools import lru_cache

def read_file(file):
    with open(file, 'r') as file:
        return [int(x) for x in file.read().split()]

def next_state(n):
    if n == 0:
        return [1]
    elif len(str(n)) % 2 == 0:
        return [int(str(n)[:len(str(n))//2]), int(str(n)[len(str(n))//2:])]
    else:
        return [n*2024]

@lru_cache(maxsize=None)
def nb_children(stone, n):
    if n == 0:
        return 1
    dc = next_state(stone)
    return sum([nb_children(c, n-1) for c in dc])
   

def part1(l):
    s = 0
    for stone in l:
        s += nb_children(stone, 25)
    return s
        
def part2(l):
    s = 0
    for stone in l:
        s += nb_children(stone, 75)
    return s


if __name__ == "__main__":
    l = read_file("11/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))