from collections import deque

N, M = map(int, input().split(" "))
A = list(map(int, input().split()))

def make_divisors(n, P):
    i = 1
    while (i*i <= n) & (i <= M) :
        if n % i == 0:
            P[i] = 1
            if i != n // i:
                P[n//i] = 1
        i += 1
    return 0


P = [0]*(M+1)
P[0] = 1
for ai in A:
    make_divisors(ai,P)
P[1]=0

def is_divisors(n, P):
    i = 1
    while (i*i <= n) & (i <= M) :
        if n % i == 0:
            if P[i] == 1: return False
            if (i != n // i) & ((n//i)<=M) & (P[n//i] == 1): return False
        i += 1
    return True

d = deque()
for mi in range(1, M+1):
    if is_divisors(mi,P): d.append(mi)



print(len(d))
while(d):
    print(d.popleft())