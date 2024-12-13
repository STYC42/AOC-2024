
from dataclasses import dataclass
from typing import Set

@dataclass
class Vector:
    x : int
    y : int

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __hash__(self):
        return hash(('vector', self.x, self.y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def corr(self, l):
        return 0 <= self.y < l.height and 0 <= self.x < l.width
    
    def right(self):
        return Vector(self.x + 1, self.y)
    
    def left(self):
        return Vector(self.x - 1, self.y)
    
    def up(self):
        return Vector(self.x, self.y-1)
    
    def down(self):
        return Vector(self.x, self.y+1)
    
    def neigh(self):
        return [self.right(), self.left(), self.up(), self.down()]
    
class Map(list):
    def __getitem__(self, key):
        if isinstance(key, Vector):
            return super().__getitem__(key.y)[key.x]
        return super().__getitem__(key)
    
    @property
    def height(self):
        return len(self)
    
    @property
    def width(self):
        return len(self[0])
    
    @property
    def area(self):
        return self.height * self.width
    
    def enumerate(self):
        for y, line in enumerate(self):
            for x, v in enumerate(line):
                yield Vector(x, y), v

def read_file(file):
    with open(file, "r") as f:
        return [list(line.strip()) for line in f]

def same_neighbours(pos: Vector, l: Map):
    for neighbour in pos.neigh():
        if neighbour.corr(l) and l[neighbour] == l[pos]:
            yield neighbour

def get_areas(l: Map):
    not_processed = {pos for pos, v in l.enumerate()}
    areas = []
    while not_processed:
        new_area = set()
        pile = [not_processed.pop()]
        while pile:
            pos = pile.pop()
            for neighbour in same_neighbours(pos, l):
                if neighbour in not_processed:
                    pile.append(neighbour)
            new_area.add(pos)
            not_processed.discard(pos)
        areas.append(new_area)
    return areas

def edges(l: Map):
    shh = set()
    shl = set()
    svl = set()
    svr = set()
    for pos, v in l.enumerate():
        if not pos.up().corr(l):
            shh.add(pos)
        if not pos.left().corr(l):
            svl.add(pos)
        if not pos.right().corr(l):
            svr.add(pos)
        if not pos.down().corr(l):
            shl.add(pos)
        if pos.down().corr(l) and l[pos] != l[pos.down()]:
            shh.add(pos.down())
            shl.add(pos)
        if pos.right().corr(l) and l[pos] != l[pos.right()]:
            svl.add(pos.right())
            svr.add(pos)
    return shh, shl, svl, svr

def grp(edg: Set[Vector], dir: bool):
    """
    dir: True for horizontal, False for vertical
    """
    key = lambda v: (v.y, v.x) if dir else (v.x, v.y)
    edg = sorted(edg, key=key)
    groups = [[edg[0]]]
    prec = edg[0]
    for edge in edg[1:]:
        if dir:
            if edge.left() == prec:
                groups[-1].append(edge)
            else:
                groups.append([edge])
        else:
            if edge.up() == prec:
                groups[-1].append(edge)
            else:
                groups.append([edge])
        prec = edge
    return groups

def part1(l):
    s = 0
    l = Map(l)
    areas = get_areas(l)
    shh, shl, svl, svr = edges(l)
    for area in areas:
        edg = (len(area & shh) +
               len(area & shl) +
               len(area & svl) +
               len(area & svr))
        s += len(area)*edg
    return s
        
def part2(l):
    s = 0
    l = Map(l)
    areas = get_areas(l)
    shh, shl, svl, svr = edges(l)
    for area in areas:
        ehh = area & shh
        ehl = area & shl
        evl = area & svl
        evr = area & svr
        borders = len(grp(ehh, True) + 
                      grp(ehl, True) + 
                      grp(evl, False) + 
                      grp(evr, False))
        s += borders*len(area)
    return s

if __name__ == "__main__":
    l = read_file("12/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))