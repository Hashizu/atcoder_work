#!/usr/bin/env python3
import sys
from copy import deepcopy
ans = [0]
def rev(W,H,k,i,a):
    temp = k[i//W][i%W]
    # print(i//W,i%W)
    k_1 = deepcopy(k[:])
    k_2 = deepcopy(k[:])
    # print(k_2)

    if (a>0)and(temp==0) and (i//W < (H-1)) and (k[i//W+1][i%W]==0): # 下が空いてる
        k_1[i//W][i%W] = 1
        k_1[i//W+1][i%W] = 1
        # print(i//W,i%W)
        # print("u")
        rev(W,H,k_1,i+1,a-1)
    if (a>0)and(temp==0) and (i%W < (W-1)) and (k[i//W][i%W+1]==0): # 右が空いてる
        # k_ = copy(k)
        k_2[i//W][i%W] = 1
        k_2[i//W][i%W+1] = 1
        # print(i//W,i%W)
        # print("r")
        # print(i,a,k_2)
        rev(W,H,k_2,i+1,a-1)
    # print(i,a,k)
    if (i==H*W-1) and (a==0):
        ans[0]+=1
    if i+1<H*W:
        rev(W,H,k,i+1,a)



def solve(H: int, W: int, A: int, B: int):

    k = [[0]*W for _ in range(H)]
    # ans = [0]

    rev(W,H,k,0,A)
    print(ans[0])

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(H, W, A, B)

if __name__ == '__main__':
    main()
