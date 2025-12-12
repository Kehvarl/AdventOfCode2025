from collections import defaultdict, deque
from pprint import pprint
from functools import cache

with open("input.txt") as f:
    content = f.read()
    # content = [int(x) for x in f.readlines()]

def rotate(present):
    newshape = []
    for y in range(len(present)):
        newline = ""
        for x in range(len(present[0])):
            newline += present[2-x][y]
        newshape.append(newline)
    return newshape

def flip(present):
    new_shape = []
    for line in range(len(present)):
        new_shape.append(present[2-line])
    return new_shape

def rotate_and_flip(shape):
    variants = set()
    for turn in range(4):
        shape = rotate(shape)
        variants.add(tuple(shape))
        variants.add(tuple(flip(shape)))
    return [list(s) for s in variants]

def draw(present):
    for y,line in enumerate(present):
        newline = ""
        for x,c in enumerate(line):
            newline += c
        print(newline)
    print()


blob = content.split("\n\n")
blob2 = blob[-1]
presents = {}
for p in blob[:-1]:
    id, p = p.split(":")
    shape = p.strip().split("\n")
    simple = ""
    squares = 0
    for y, line in enumerate(shape):
        for x, c in enumerate(line):
            if c == "#":
                simple += "1"
                squares += 1
            else:
                simple += "0"

    presents[int(id)] = (int(simple), squares)

regions = []
for r in blob2.strip().split("\n"):
    size, shapes = r.split(":")
    sx,sy = size.split("x")
    shapes = tuple([int(s) for s in shapes.strip().split()])
    regions.append((int(sx), int(sy), shapes))


valid = 0
for r in regions:
    rx, ry, r_shapes = r
    ra = rx * ry

    required_area = sum(
        count * presents[idx][1] for idx, count in enumerate(r_shapes)
    )
    print(rx, ry, ra, r_shapes, required_area)

    if ra >= required_area:
        valid += 1

print(valid)
