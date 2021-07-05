import numpy as np

N, K= map(int, input().split())

A = []
for _ in range(N):
    A.append([int(x) for x in input().split()])
A = np.array(A)

min_median = 10**9
p = K**2 - K**2//2-1

for i in range(0, N-K+1):
    for j in range(0, N-K+1):
        # print(np.sort(A[i:i+K,j:j+K].flatten()))
        med= np.sort(A[i:i+K,j:j+K].flatten())[p]
        min_median = min(med, min_median)
print(min_median)