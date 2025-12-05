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
    fresh.append([int(start), int(end) + 1])

good = set()
bad = set()
for h in have.strip().split("\n"):
    test = int(h)
    for f in fresh:
        if f[0] <= test <= f[1]:
            good.add(int(h))
        else:
            bad.add(int(h))

print(len(good), good)
print(len(bad), bad)