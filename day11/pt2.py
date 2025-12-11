from collections import defaultdict, deque
from functools import cache
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

devices = {}
for line in content:
    tag, contents = line.split(": ")
    contents = contents.split()
    devices[tag] = contents

#pprint(devices)
@cache
def dfs(start, paths):
    if start == 'out':
        if paths == ('dac', 'fft'): return 1
        return 0
    if start in ('dac', 'fft'):
        paths = set(paths)
        paths.add(start)
        paths = tuple(sorted(paths))
    return sum(dfs(n, paths) for n in devices[start])


print(dfs('svr', tuple()))
