from collections import Counter

def main(l, r):
    s = 0
    c = Counter(l)
    d = Counter(r)
    for k in c:
        s += k*c[k]*d[k]
    print(s)


l = []
r = []
for line in open("1/input.txt"):
    a, b = map(int, line.strip().split())
    l.append(a)
    r.append(b)
main(l, r)