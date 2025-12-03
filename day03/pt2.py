from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

def scan(bank, start, count):
    best = 0
    i= 0
    for c in range(start, len(bank)-(count-1)):
        v = int(bank[c])
        if v > best:
            best = v
            i = c
    return i, best

banks = []
total = 0
for line in content:
    batteries = 12
    i = -1
    for c in range(batteries, 0, -1):
        i, b = scan(line, i+1, c)
        #print(i, b, c, b*(10**(c-1)))
        total += b*(10**(c-1))

print(total)
