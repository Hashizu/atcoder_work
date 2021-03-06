#!/usr/bin/env python3
import sys


def solve(N: int, P: int, S: int):

    co = 0
    for l in range(1, N): # l は開始位置
        for x in range(10 ** N // P):
            for nn in range(1,N):
                print(S[N-nn:-l])
                if int(S[l-nn:-l]) == x*P :
                    co= co+1
                    break
            if nn == N: break  
            # 一つ目の約数あり
    print(co)

    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    S = str(next(tokens)).replace("\n", "")
    solve(N, P, S)

if __name__ == '__main__':
    main()
