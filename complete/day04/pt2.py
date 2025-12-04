from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

neighbors = [(-1,-1), (-1,0), (-1,1),(0,-1), (0,1),(1,-1), (1,0), (1,1)]

def step(content):
    removed = 0
    out = []
    for y, v1 in enumerate(content):
        line = ""
        for x, v2 in enumerate(v1):
            if v2 == ".":
                line += v2
                continue
            rolls = 0
            for n in neighbors:
                dx,dy = n
                tx = x + dx
                ty = y + dy
                if 0 <= tx < len(v1) and 0 <= ty < len(content):
                    if content[ty][tx] == "@":
                        rolls += 1
            if rolls <4:
                removed += 1
                line += "."
            else:
                line += v2
        out.append(line)
    return out, removed


out, removed = step(content)
steps = 1
total = 0
while removed > 0:
    #pprint(removed)
    steps += 1
    total += removed
    out, removed = step(out)

pprint(out)
print(steps, total)