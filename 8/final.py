from dataclasses import dataclass

@dataclass
class Vector:
    x: int
    y: int
    
    def __add__(self, other: "Vector"):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Vector"):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def copy(self):
        return Vector(self.x, self.y)

def read_file(file):
    with open(file, 'r') as file:
        return [line.strip() for line in file]
    
def get_antennas(l):
    return [(c, Vector(j, i)) for i, line in enumerate(l) for j, c in enumerate(line) if c != "."]
   
def inbound(l, pos: Vector):
    return 0 <= pos.y < len(l) and 0 <= pos.x < len(l[0])
   
def part1(l):
    antennas = get_antennas(l)
    rpos = set()
    for f in antennas:
        for s in antennas:
            c1, pos1 = f
            c2, pos2 = s
            if c1 == c2 and f != s:
                vec = pos2 - pos1
                r = pos2 + vec
                if inbound(l, r):
                    rpos.add(r)
    return len(rpos)         
        
def part2(l):
    antennas = get_antennas(l)
    rpos = set()
    for f in antennas:
        for s in antennas:
            c1, pos1 = f
            c2, pos2 = s
            if c1 == c2 and f != s:
                vec = pos2 - pos1
                r = pos1
                while inbound(l, r):
                    rpos.add(r)
                    r = r - vec
    return len(rpos)


if __name__ == "__main__":
    l = read_file("8/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))