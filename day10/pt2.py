from collections import defaultdict, deque
from pprint import pprint

with open("test.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

machines = [line.split() for line in content]
better_machines = []

for m in machines:
    lights = 0
    for i,l in enumerate(reversed(m[0][1:-1])):
        if l == "#":
            lights |= (1 << int(i))
    jolts = [int(i) for i in m[-1][1:-1].split(",")]
    buttons = []
    for b in m[1:-1]:
        button = [0 for _ in range(len(m[0][1:-1]))]
        for i in b[1:-1].split(','):
            button[int(i)] = 1
        buttons.append(button)

    better_machines.append([lights, buttons, jolts])


for m in better_machines:
    print(solve_linear(m[2], m[1], None, float("inf"), 0, [0 for _ in range(len(m[2]))], 0, []))

