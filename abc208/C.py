import numpy as np

N, K = map(int, input().split())
# a =[0]*N
a = [a_ for a_ in map(int, input().split())]

base = K // N
rem = K % N
ap = [-1]*N
for i, m in enumerate(np.argsort(a)):
    ap[m] = i

for k in ap:
    if k+1 > rem: print(base)
    else: print(base+1)