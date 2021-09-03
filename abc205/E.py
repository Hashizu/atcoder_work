N, M, K= map(int, input().split())

MOD = 10**9 + 7

S = [[0]*(M+1) for i in range(N+1)]

for i in range(1,M+1):
    S[0][i] = 1

for i in range(1,K+1):
    S[i][0] = 1
# print(S)

for wi in range(1, N+1):
    for bi in range(max(1,wi-K), M+1):
        k = 0 if wi-1<0 else S[wi-1][bi]
        l = 0 if bi-1<0 else S[wi][bi-1]

        S[wi][bi]= (k+l) %MOD

# print(S)

print(S[wi][bi])
