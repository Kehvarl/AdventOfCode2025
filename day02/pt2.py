from collections import defaultdict, deque
from operator import truediv
from pprint import pprint

with open("input.txt") as f:
    content = f.readline().strip()
    # content = [int(x) for x in f.readlines()]

def get_substrings(s):
    for x in range(1,len(s)):
        sub = s[:x]
        if sub * (len(s) // len(sub)) == s:
            return True
    return False

content = content.split(",")
total = 0
for r in content:
    start, end = r.split("-")
    start = int(start)
    end = int(end)
    for val in range(start, end+1):
        s = str(val)
        l = s[:len(s)//2]
        r = s[len(s)//2:]
        if get_substrings(s):
            #print(s, l, r)
            total += val

print(total)