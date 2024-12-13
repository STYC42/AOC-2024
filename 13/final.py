import re
from dataclasses import dataclass

@dataclass
class Vector:
    x : int
    y : int

    @classmethod
    def det(cls, a, b):
        return a.x*b.y - a.y*b.x

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

def read_file(file):
    with open(file) as f:
        lines = f.readlines()
        games = [game for game in zip(lines[::4], lines[1::4], lines[2::4])]
    return games
   
def decrypt_game(game):
    pattern_button = r"Button\s[A-Z]:\sX\+(\d+),\sY\+(\d+)"
    pattern_prize = r"Prize:\sX=(\d+),\sY=(\d+)"
    A = re.match(pattern_button, game[0])
    B = re.match(pattern_button, game[1])
    P = re.match(pattern_prize, game[2])
    Av = Vector(int(A.group(1)), int(A.group(2)))
    Bv = Vector(int(B.group(1)), int(B.group(2)))
    Pv = Vector(int(P.group(1)), int(P.group(2)))
    return Av, Bv, Pv

def solve(A, B, P):
    D = Vector.det(A, B)
    if D == 0:
        return None
    a = Vector.det(P, B) / D
    b = Vector.det(A, P) / D
    if a == int(a) and b == int(b) and a >= 0 and b >= 0:
        return 3*int(a) + int(b)
    return None

def part1(l):
    s = 0
    for game in l:
        A, B, P = decrypt_game(game)
        if (res := solve(A, B, P)) is not None:
            s += res
    return s  
        
def part2(l):
    s = 0
    for game in l:
        A, B, P = decrypt_game(game)
        P = P + Vector(10000000000000, 10000000000000)
        if (res := solve(A, B, P)) is not None:
            s += res
    return s


if __name__ == "__main__":
    l = read_file("13/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))