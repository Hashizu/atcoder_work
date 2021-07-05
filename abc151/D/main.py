#!/usr/bin/env python3
import sys
# Maze by warshall_floyd
# ワーシャルフロイド法


def solve(H, W, a):
    # print(a)
    inf = H*W**2
    d = [[inf]*(H*W) for _ in range(H*W)]
    for h in range(H):
        for w in range(W):
            if (a[h][w] == "0"):
                d[h*W+w][h*W+w] = 0
                if (w+1<W)and(a[h][w+1] == "0"):
                    d[h*W+w][h*W+w+1] = 1
                if (h+1<H)and(a[h+1][w] == "0"):
                    d[h*W+w][(h+1)*W+w] = 1
                if (w-1>=0)and(a[h][w-1] == "0"):
                    d[h*W+w][h*W+w-1] = 1
                if (h-1>=0)and(a[h-1][w] == "0"):
                    d[h*W+w][(h-1)*W+w] = 1
                
    # print(*d, sep='\n')

    for k in range(H*W):  # via k [k//W][k% W]
        for st in range(H*W):  # start from st
            for ed in range(H*W):  # go to ed
                d[st][ed] = min(d[st][ed], d[st][k]+d[k][ed])

    # print(*d, sep="\n")

    print(max(*map(lambda x: max([_ if _ != inf else 0 for _ in x ]), d)))
    return

if __name__ == '__main__':
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int

    a = [[_ for _ in next(tokens).replace(".","0").replace("#","1")] for _ in range(H)]  # type: "List[int]"
    solve(H, W, a)
