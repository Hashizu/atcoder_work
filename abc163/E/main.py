#!/usr/bin/env python3
import sys
import numpy as np

def solve(N: int, A: "List[int]"):
    a=np.argsort(A)[::-1]

    dp = np.zeros((N+1,N+1), dtype=np.int)
    for i, a_ind in enumerate(a):

        x_p_y = i+1
        a_ = A[a_ind]

        for x in range(0, x_p_y+1):
            y = x_p_y - x
            if x-1<0: x_add = 0
            else : x_add = dp[x-1, y] + a_*abs(a_ind-x+1)
            if y-1<0: y_add = 0
            else : y_add = dp[x, y-1] + a_*abs(N-y - a_ind)
            dp[x, y] = max(x_add, y_add)

    print(np.max(dp))

    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
