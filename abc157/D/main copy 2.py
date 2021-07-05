#!/usr/bin/env python3
import sys
from collections import deque

class prof:
    def __init__(self, num):
        self.num = num
        self.friends = deque([])
        self.blocks = deque([])        
        self.clus = -1
        self.ca = 0

    def set_friends(self, fre):
        self.friends.append(fre)

    def set_blocks(self, blo):
        self.blocks.append(blo)

    def set_clus(self, cl):
        self.clus = cl

    def set_ca(self, ca):
        self.ca = ca
    


def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):

    nodes = [prof(i) for i in range(N)]

    for ai, bi in zip(A, B):
        nodes[ai-1].set_friends(bi)
        nodes[bi-1].set_friends(ai)
    for ai, bi in zip(C, D):
        nodes[ai-1].set_blocks(bi)
        nodes[bi-1].set_blocks(ai)
    
    cl = 0
    ser = set(range(1,N+1))
    finished = []
    while len(finished) != N:
        # cl +=1 
        q = deque([list(ser - set(finished))[0]])
        f_temp = []
        while bool(q):
            temp = q.popleft()
            if temp not in f_temp:
                # nodes[temp-1].set_clus(cl)
                f_temp.append(temp)
                for t in nodes[temp-1].friends:
                    if t not in f_temp : q.append(t)
            f_set = set(f_temp)
            for gr in f_temp:
                fr = set(nodes[gr-1].friends)
                bl = set(nodes[gr-1].blocks)
                nodes[gr-1].set_ca(len(f_set - fr - bl)-1)
        finished.extend(f_temp)

    print(*[x.ca for x in nodes])

    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (K)  # type: "List[int]"
    D = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, K, A, B, C, D)

if __name__ == '__main__':
    main()
