from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]
dial = 50
zeros = 0

for line in content:
    d = line[0]
    count = int(line[1:])
    if d == "L":
        dial =  (dial - count) % 100
    else:
        dial =  (dial + count) % 100

    print(line, dial)
    if dial == 0:
        zeros += 1

print(zeros)
