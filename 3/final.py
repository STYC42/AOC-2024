def read_file(file):
    with open(file) as f:
        return f.read()
   
import re
   
def part1(txt):
    pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
    results = re.findall(pattern, txt)
    return sum(int(a) * int(b) for a, b in results)
      
def part2(txt):
    parts = txt.split("do()")
    executable_parts = [code.split("don't()")[0] for code in parts]
    return sum(part1(code) for code in executable_parts)


if __name__ == "__main__":
    l = read_file("3/input.txt")
    print("part1 :", part1(l))
    print("part2 :", part2(l))