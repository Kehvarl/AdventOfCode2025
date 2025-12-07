from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

beams = set()
all_beams = set()
splits = 0
for x, v2 in enumerate(content[0]):
    if v2 == "S":
        beams.add((x,0))
        all_beams.add((x, 0))

while beams:
    b = beams.pop()
    bx, by = b
    by += 1
    if by < len(content):
        if content[by][bx] == "^":
            splits += 1
            if bx-1 >= 0:
                beams.add((bx-1, by))
                all_beams.add((bx - 1, by))
            if bx+1 < len(content[0]):
                beams.add((bx+1, by))
                all_beams.add((bx + 1, by))
        else:
            beams.add((bx, by))
            all_beams.add((bx, by))


splits = 0
skips = 0
for y, v1 in enumerate(content):
    line = ""
    for x, v2 in enumerate(v1):
        if (x,y) in all_beams:
            line += "|"
        else:
            if v2 == "^":
                if (x, y-1) not in all_beams:
                    line += "X"
                    skips += 1
                else:
                    line += v2
                    splits += 1
            else:
                line += v2
    print(line)

print(splits, skips)




