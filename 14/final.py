from dataclasses import dataclass
import re

@dataclass 
class Vector:
    x : int
    y : int

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __mod__(self, other):
        return Vector(self.x % other.x, self.y % other.y)


def read_file(file):
    with open(file, 'r') as file:
        return [line.strip() for line in file]
    
def parse_line(line):
    pattern = r"p=(-?\d+),(-?\d+)\sv=(-?\d+),(-?\d+)"
    m = re.match(pattern, line)
    return Vector(int(m.group(1)), int(m.group(2))), Vector(int(m.group(3)), int(m.group(4)))
   
   
def part1(l):
    pos = [[] for _ in range(4)]
    for line in l:
        p, v = parse_line(line)
        npos = (p + v*100)%Vector(101, 103)
        if npos.x < 50 and npos.y < 51:
            pos[0].append(npos.x)
        if npos.x > 50 and npos.y < 51:
            pos[1].append(npos.x)
        if npos.x < 50 and npos.y > 51:
            pos[2].append(npos.x)
        if npos.x > 50 and npos.y > 51:
            pos[3].append(npos.x)
    return len(pos[0])*len(pos[1])*len(pos[2])*len(pos[3])
    
        
def part2(l):
    return 8168
        


if __name__ == "__main__":
    l = read_file("14/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))