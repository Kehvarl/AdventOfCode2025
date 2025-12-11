from collections import defaultdict, deque
from functools import cache
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
@cache
def dfs(start, seen):
    if start in ('dac', 'fft'):
        seen = set(seen)
        seen.add(start)
        seen = tuple(sorted(seen))

    if start == 'out':
        if seen == ('dac', 'fft'):
            return 1
        return 0

    out = 0
    for n in devices[start]:
        out += dfs(n, seen)

    return out

print(dfs('svr', ()))