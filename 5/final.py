
def read_file(file):
    with open(file, 'r') as file:
        return [line.strip() for line in file]


def inf(a, b, d):
    # Vérifie si a peut être avant b
    if a in d:
        if b in d[a]:
            return False
    return True

def correct(n, d):
    # Vérifie si n est correct
    for i, b in enumerate(n):
        for a in n[:i]:
            if not inf(a, b, d):
                return False
    return True

def sort(n, d):
    # Trie n selon d
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if not inf(n[i], n[j], d):
                n[i], n[j] = n[j], n[i]
    return n

def read_input(l):
    # Stocke les exigences dans d et les différentes listes dans s
    d = {}
    s = []
    exg = True
    for line in l:
        if not line:
            exg = False
            continue
        if exg:
            a, b = map(int, line.split("|"))
            if b not in d:
                d[b] = [a]
            else:
                d[b].append(a)
        else:
            n = list(map(int, line.split(",")))
            s.append(n)
    return d, s
   
def part1(l):
    # Ne prendre que les listes déjà correctes
    d, s = read_input(l)
    c = 0
    for n in s:
        if correct(n, d):
            c += n[len(n)//2]
    return c
        
def part2(l):
    # On ne prend que les listes incorrectes
    # On les "trie" avec un algorithme ma foi, absolument ignoble, je sais (mais ça fonctionne)
    d, s = read_input(l)
    c = 0
    for n in s:
        if not correct(n, d):
            n = sort(n, d)
            c += n[len(n)//2]
    return c
             


if __name__ == "__main__":
    l = read_file("5/input.txt")
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))