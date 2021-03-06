#!/usr/bin/env python3
import sys

def solve(N: int, u: "List[int]", v: "List[int]", w: "List[int]"):

    G=[dict() for i in range(N)]
    for i in range(N-1):
        ui,vi,wi=u[i],v[i],w[i]
        G[ui-1][vi-1]=wi
        G[vi-1][ui-1]=wi

    dist = [-1]*N
    p = [0]
    dist[0] = 0

    while (len(p)>0):
        k = p.pop()
        for n in G[k]:
            if dist[n]==-1:
                dist[n] = dist[k] + G[k][n]
                p.append(n)
    
    for x in dist:
        print(x%2)

    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    w = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, u, v, w)

if __name__ == '__main__':
    main()
