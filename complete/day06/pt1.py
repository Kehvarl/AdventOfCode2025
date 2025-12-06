from collections import defaultdict, deque
from pprint import pprint

from debian.debtags import output

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

problems = [[0 for _ in range(len(content))] for _ in range(len(content[0].split()))]

for y, line in enumerate(content):
    #print(line)
    cols = [c.strip() for c in line.split()]
    for x, c in enumerate(cols):
        problems[x][y] = c

sum = 0
for p in problems:
    op = p[-1]
    if op =="*":
        output = int(p[0])
        for v in p[1:-1]:
            output *= int(v)
    elif op =="/":
        output = int(p[0])
        for v in p[1:-1]:
            output /= int(v)
    elif op == "+":
        output = int(p[0])
        for v in p[1:-1]:
            output += int(v)
    elif op == "-":
        output = int(p[0])
        for v in p[1:-1]:
            output -= int(v)
    else:
        print(p)
    #print(output)
    sum += output

print(sum)