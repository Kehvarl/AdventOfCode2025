from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

banks = []
total = 0
for line in content:
    best = 0
    i = 0
    for c in range(len(line)-1):
        v = int(line[c])
        if v > best:
            best = v
            i = c
    b2 = 0
    i2 = 0
    for c in range(i+1, len(line)):
        v = int(line[c])
        if v > b2:
            b2 = v
            i2 = c
    #print(i, best, i2, b2)
    #print(best, b2)
    total += best*10
    total += b2
print(total)
