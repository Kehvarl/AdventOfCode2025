from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

devices = defaultdict(list)
for line in content:
    tag, contents = line.split(": ")
    contents = contents.split()
    devices[tag] = contents

#pprint(devices)

def dfs(devices, start, end, path, allPaths):
    visited = {start}
    path.append(start)

    if start == end:
        allPaths.append(path.copy())
    else:
        for next in devices[start]:
            dfs(devices, next, end, path, allPaths)

    path.pop()

all = []
dfs(devices,'you', 'out', [], all)

pprint(all)
print(len(all))