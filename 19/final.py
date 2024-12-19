from functools import lru_cache
from tqdm import tqdm

def read_file(file):
    with open(file, 'r') as file:
        return file.read().splitlines()
        
def decrypt(l):
    patterns = l[0].split(', ')
    towers = l[2:]
    return patterns, towers

@lru_cache(maxsize=None)
def possible(patterns, tower):
    s = 0
    for pat in patterns:
        if tower.startswith(pat):
            if tower == pat:
                s += 1
            if (r := possible(patterns, tower[len(pat):])):
                s += r
    return s
   
def part1(l):
    s = 0
    patterns, towers = decrypt(l)
    for tower in tqdm(towers, leave=False):
        if (r := possible(tuple(patterns), tower)):
            s += 1
    return s
        
def part2(l):
    s = 0
    patterns, towers = decrypt(l)
    for tower in tqdm(towers, leave=False):
        if (r := possible(tuple(patterns), tower)):
            s += r
    return s

if __name__ == "__main__":
    l = read_file("19/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))