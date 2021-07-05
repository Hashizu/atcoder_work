N, K= map(int, input().split())

A = [[0] for i in range(N)]
B = [[0] for i in range(N)]

for i in range(N):
    A[i], B[i]= map(int, input().split())

f = [(a,b) for a,b in zip(A,B)]
f = sorted(f)

s = K
n = 0
for i in range(N):
    ai,bi = f[i]
    if n+s < ai: break
    else:
        s = s - (ai-n) + bi
        n = ai

print(n+s)
