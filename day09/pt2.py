from collections import defaultdict, deque
from pprint import pprint

from samba import fault_setup

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

tiles = []
for v1 in content:
    x, y =[int(v) for v in v1.split(",")]
    tiles.append((x,y))

def area (a,b):
    #print((abs(a[0] - b[0]) + 1), (abs(a[1] - b[1]) + 1))
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

green = set()
for i in range(len(tiles)-1):
    t1 = tiles[i]
    t2 = tiles[i + 1]
    if t1[0] > t2[0] or t1[1] > t2[1]:
        t1, t2 = t2, t1
    for y in range(t1[1], t2[1]+1):
        for x in range(t1[0], t2[0]+1):
            green.add((x,y))

largest = [0, (), ()]
for t1 in tiles:
    for t2 in tiles:
        a = area(t1, t2)
        if a > largest[0]:
            best = True
            for i, t in enumerate(tiles):
                tn = tiles[(i+1) % len(tiles)]
                # Check the rectangle does not extend outside the overall polygon
                if not ((t[1] >= max(t1[1], t2[1])) and (tn[1] >= max(t1[1], t2[1])) \
                    or (t[1] <= min(t1[1], t2[1])) and (tn[1] <= min(t1[1], t2[1])) \
                    or (t[0] >= max(t1[0], t2[0])) and (tn[0] >= max(t1[0], t2[0])) \
                    or (t[0] <= min(t1[0], t2[0])) and (tn[0] <= min(t1[0], t2[0]))):
                    best = False
                    break
            if best:
                largest = [a,t1,t2]
print(largest)
