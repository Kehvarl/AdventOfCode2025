from collections import defaultdict, deque, Counter
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

beams = [] #set()
splitters = defaultdict(int)
splits = 0
start = None
for x, v2 in enumerate(content[0]):
    if v2 == "S":
        start = x
        break

quantum = Counter({start: 1})

for y, v1 in enumerate(content[1:]):
    new_quantum = Counter()
    for x in quantum:
        c = quantum[x]
        if v1[x] == "^":
            new_quantum[x-1] += c
            new_quantum[x+1] += c
        else:
            new_quantum[x] += c
    quantum = new_quantum

sum = 0
for x in quantum:
    sum += quantum[x]
print(sum)
