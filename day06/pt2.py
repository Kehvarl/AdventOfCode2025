from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

problems = [["" for _ in range(len(content))] for _ in range(len(content[0].split()))]

working = defaultdict(str)
for y, line in enumerate(content):
    for x, c in enumerate(line):
        working[(x, y)] = c


problems = []
pi = 0
problem = []
for y in range(len(content[0])):
    val = ""
    for x in range(len(content)):
        if working[(y,x)].isnumeric():
            val += working[(y,x)]
        elif working[(y,x)] in ["*", "+"]:
            op = working[(y,x)]
    if val != '':
        problem.append(val)
    else:
        problem = list(reversed(problem))
        problem.append(op)
        problems.append(problem)
        problem = []


sum = 0
for p in problems:
    print(p)
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