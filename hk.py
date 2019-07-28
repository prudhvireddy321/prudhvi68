import sys, string, math, itertools

s = input()
s = int(s)
L = []

for i in range(0,s) :
    r = input()
    L.append(r)

common_prefix = []
for i in zip(*L):
    if i.count(i[0]) == len(i):
        common_prefix.append(i[0])
    else:
        break
ans = ''.join(common_prefix)
print(ans)
