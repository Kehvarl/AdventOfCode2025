from collections import defaultdict, deque
from ctypes.wintypes import tagPOINT
from pprint import pprint
import math

class UnionFind:
    def __init__(self):
        self.parent = {}

    def make_set(self, elements):
        for element in elements:
            self.parent[element] = element

    def find(self, element):
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, element1, element2):
        root1 = self.find(element1)
        root2 = self.find(element2)
        if root1 != root2:
            self.parent[root1] = root2



with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

def distance (a, b):
    ax,ay,az = a
    bx,by,bz = b
    dx = ax - bx
    dy = ay - by
    dz = az - bz
    return math.sqrt(dx**2 + dy**2 + dz**2)


boxes = []
for line in content:
    x,y,z = [int(x) for x in line.split(',')]
    boxes.append((x,y,z))

distances = {}
for b in boxes:
    for b1 in boxes:
        if b == b1:
            continue
        distances[distance(b, b1)] = (b, b1)


uf = UnionFind()
uf.make_set(boxes)

keys = sorted(distances.keys())
for i in range(1000):
    a,b = distances[keys[i]]
    uf.union(a,b)

circuits = {}
for i in range(len(boxes)):
    circuits[boxes[i]] = 0
for i in range(len(boxes)):
    b = uf.find(boxes[i])
    circuits[b] += 1
pprint(circuits)
top = []
for c in circuits:
    top.append(circuits[c])

s = sorted(top)
print(s[-3] * s[-2] * s[-1])