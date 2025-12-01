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
        for i in range(count, 0, -1):
            dial -= 1
            dial %= 100
            if dial == 0:
                zeros += 1
    else:
        for i in range(count, 0, -1):
            dial += 1
            dial %= 100
            if dial == 0:
                zeros += 1

    print(line, dial, zeros)


print(zeros)
