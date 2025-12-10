from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

machines = [line.split() for line in content]
better_machines = []

for m in machines:
    lights = 0
    for i,l in enumerate(reversed(m[0][1:-1])):
        if l == "#":
            lights |= (1 << int(i))
    jolts = m[-1][1:-1].split(",")
    buttons = []
    for b in m[1:-1]:
        button = 0
        bits = len(m[0][1:-1])
        for i in b[1:-1].split(','):
            button |= (1<< (bits - int(i)) -1)
        buttons.append(button)

    better_machines.append([lights, buttons, jolts])

def bfs(lights, buttons):
    q = deque([(0x0, [])])
    visited = set()
    visited.add(0x0)

    while q:
        current, path = q.popleft()

        for button in buttons:
            n = current  ^ button
            if n not in visited:
                visited.add(n)
                np = path + [n]

                if n == lights:
                    return  np

            q.append((n, np))
    return None


best =[]
for m in better_machines:
    best.append((len(bfs(m[0], m[1]))))

print(sum(best))
