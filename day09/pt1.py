from collections import defaultdict, deque
from pprint import pprint

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

largest = [0, (), ()]
while tiles:
    start = tiles.pop()
    for t in tiles:
        a = area(start, t)
        #print([a, start, t])
        if a > largest[0]:
            largest = [a, start, t]

print(largest)
