import os

N, K= map(int, input().split())

a= 0
for i in range(1, N+1):
    for j in range(1,K+1):
        a += i*100 + j
print(a)