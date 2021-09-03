S,K=input().split(" ")

S = [_ for _ in S]
K=int(K)

import itertools
p = sorted(list(set(itertools.permutations(S))))[K-1]
print("".join(p) )