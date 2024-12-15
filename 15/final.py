from dataclasses import dataclass
from tqdm import tqdm

@dataclass
class Vector:
    x: int
    y: int
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        return Vector(self.x * other, self.y * other)
    def __hash__(self):
        return hash((self.x, self.y))
    
    def correct(self, map):
        return self.x >= 0 and self.x < len(map[0]) and self.y >= 0 and self.y < len(map)
    
    def gauche(self):
        return Vector(self.x - 1, self.y)
    def droite(self):
        return Vector(self.x+1, self.y)
    def haut(self):
        return Vector(self.x, self.y-1)
    def bas(self):
        return Vector(self.x, self.y+1)
    
def read_file(file):
    with open(file, 'r') as f:
        return f.read().splitlines()
        
def decrypt(input):
    map = []
    before = True
    moves = ''
    for line in input:
        if not line:
            before = False
            continue
        if before:
            map.append(line)
        else:
            moves = moves + line
    return map, moves

def get_boxes(map):
    boxes = []
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == 'O':
                boxes.append(Vector(x, y))
    return set(boxes)

def get_walls(map):
    walls = []
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == '#':
                walls.append(Vector(x, y))
    return set(walls)

def get_robot(map):
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == '@':
                return Vector(x, y)
    return None

def depl(vec, direction):
    if direction == 0:
        return vec.haut()
    if direction == 2:
        return vec.bas()
    if direction == 3:
        return vec.gauche()
    if direction == 1:
        return vec.droite()
    return vec

def fmove(map, walls, boxes, robot, direction):
    pos = depl(robot, direction)
    obst = False
    while pos.correct(map):
        if pos in walls:
            return robot, boxes
        elif pos not in boxes:
            break
        else:
            obst = True
        pos = depl(pos, direction)
        
    if not pos.correct(map):
        raise NotImplementedError
    if obst:
        boxes.discard(depl(robot, direction))
        boxes.add(pos)
    robot = depl(robot, direction)
    
    return robot, boxes

def forward(map, walls, boxes, pos, direction):
    obst = []
    pos = depl(pos, direction)
    if pos.correct(map):
        if pos in walls or pos.gauche() in walls:
            return None
        if pos in boxes or pos.gauche() in boxes:
            if pos in boxes:
                obst.append(pos)
                if direction == 0 or direction == 2:
                    r1 = forward(map, walls, boxes, pos, direction)
                    r2 = forward(map, walls, boxes, pos.droite(), direction)
                    if r1 is None or r2 is None:
                        return None
                    obst.extend(r1)
                    obst.extend(r2)
                else:
                    r1 = forward(map, walls, boxes, pos, direction)
                    if r1 is None:
                        return None
                    obst.extend(r1)
            if pos.gauche() in boxes:
                obst.append(pos.gauche())
                if direction == 0 or direction == 2:
                    r1 = forward(map, walls, boxes, pos.gauche(), direction)
                    r2 = forward(map, walls, boxes, pos, direction)
                    if r1 is None or r2 is None:
                        return None
                    obst.extend(r1)
                    obst.extend(r2)
                else:
                    r1 = forward(map, walls, boxes, pos, direction)
                    if r1 is None:
                        return None
                    obst.extend(r1)
        return list(set(obst))
    return None
            

def fmove2(map, walls, boxes, robot, direction):
    obst = forward(map, walls, boxes, robot, direction)
    
    if obst is None:
        return robot, boxes
    for o in obst:
        assert o in boxes
        boxes.discard(o)
    for o in obst:
        boxes.add(depl(o, direction))
        
    robot = depl(robot, direction)
    
    return robot, boxes
   
def part1(l):
    map, moves = decrypt(l)
    mv = {'^': 0, '>': 1, 'v': 2, '<': 3}
    
    robot = get_robot(map)
    boxes = get_boxes(map)
    walls = get_walls(map)
    
    for move in tqdm(moves, leave=False):
        robot, boxes = fmove(map, walls, boxes, robot, mv[move])
        
    s = 0
    for box in boxes:
        s += box.x + (box.y)*100
    return s

def part2(l):
    map, moves = decrypt(l)
    mv = {'^': 0, '>': 1, 'v': 2, '<': 3}
    
    lrobot = get_robot(map)
    lboxes = get_boxes(map)
    lwalls = get_walls(map)
    
    robot = lrobot*Vector(2, 1)
    boxes = set(box*Vector(2, 1) for box in lboxes)
    walls = set(wall*Vector(2, 1) for wall in lwalls)
    map = [line*2 for line in map] # Seulement pour les dimensions
    
    for move in tqdm(moves, leave=False):
        robot, boxes = fmove2(map, walls, boxes, robot, mv[move])
        
    s = 0
    for box in boxes:
        s += box.x + (box.y)*100
    return s


if __name__ == "__main__":
    l = read_file("15/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))