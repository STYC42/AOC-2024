def main(l, r):
    s = 0
    for a, b in zip(l, r):
        s += abs(a-b)
    print(s)

l = []
r = []

for line in open("1/input.txt"):
    a, b = map(int, line.strip().split())
    l.append(a)
    r.append(b)
l.sort()
r.sort()
main(l, r)