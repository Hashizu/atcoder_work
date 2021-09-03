N,K = map(int, input().split())

C = [0]*N
for i, c in enumerate(map(int, input().split())):
    C[i] = c

cs = dict()
card = 0
max_card = 0

for i in range(K):
    if cs.get(C[i]):
        cs[C[i]] = cs[C[i]]+1
    else:
        cs[C[i]] = 1
        card+=1
max_card = max(card, max_card)

for i in range(0,N-K):
    if cs.get(C[K+i]):
        cs[C[K+i]] = cs[C[K+i]]+1
    else:
        cs[C[K+i]] = 1
        card+=1

    cs[C[i]] -= 1
    if cs[C[i]]==0:
        card -= 1
    max_card = max(card, max_card)

print(max_card)