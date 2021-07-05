#!/usr/bin/env python3
import sys


def solve(H, W, a):
    print(a)
    
    dep = []
    i_l = []

    for fy in range(H):
        for fx in range(W):
            if a[fy][fx] != "0": continue
            a_ = a.copy()
            same_depths = []
            next_depths = [(fy, fx)]
            i = -1
            while(len(next_depths) > 0):
                i+=1
                for q in next_depths:
                    if a_[q[0]][q[1]] != "0": continue
                    a_[q[0]][q[1]] = "1"

                    if (q[0] > 0) and (a_[q[0]-1][q[1]] =="0"):
                        same_depths.append((q[0]-1, q[1]))
                        # a_[q[0]-1][q[1]] = "1"
                    if (q[1] > 0) and (a_[q[0]][q[1]-1] =="0"):
                        same_depths.append((q[0], q[1]-1))
                            # a_[q[0]][q[1]-1] = "1"
                    if (q[0]+1 < H) and (a_[q[0]+1][q[1]] =="0"):
                        same_depths.append((q[0]+1, q[1]))
                        # a_[q[0]+1][q[1]] = "1"
                    if (q[1]+1 < W) and (a_[q[0]][q[1]+1] =="0"):
                        # a_[q[0]][q[1]+1] = "1"
                        same_depths.append((q[0], q[1]+1))
                
                next_depths = same_depths

            i_l.append(i)

    print(max(i_l))
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
