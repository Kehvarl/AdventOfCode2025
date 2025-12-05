from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    raw = f.read()
    #content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

range_fresh, have = raw.split("\n\n")

fresh = []
for line in range_fresh.split("\n"):
    start, end = line.split("-")
    fresh.append((int(start), int(end)))

fresh.sort()
total = 0
high = 0
for s,e in fresh:
    print(high, s, e)
    if high < s:
        total += (e - s + 1)
        high = e + 1
    elif high <= e:
        total += (e - high + 1)
        high = e + 1

print(total)