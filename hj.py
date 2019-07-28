import sys, string, math
n = int(input())
L = list(map(int,input().split()))
L2 = []
for i in range(n) :
    if L[i] == i : L2.append(i)
L3 = sorted(L2)
if len(L3) == 0 : print(-1)
else :     print(*L3)
