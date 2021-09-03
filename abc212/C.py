N,M = map(int, input().split(" "))

A = sorted(map(int, input().split(" ")))
B = map(int, input().split(" "))

min_abs = 10**9
import bisect
for bi in B:
    c = bisect.bisect_left(A, bi)
    if c == len(A):
        min_abs = min([abs(bi-A[c-1]),min_abs])
    elif c == 0:
        min_abs = min([abs(A[c]-bi),min_abs])
    else:
        min_abs = min([abs(A[c]-bi),abs(bi-A[c-1]),min_abs])

print(min_abs)

