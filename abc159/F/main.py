#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int


def solve(N: int, S: int, A: "List[int]"):

    st = N*(N+1)//2 % MOD
    cnt = 0

    for x in range(N):
        temp = A[x]
        if temp == S:
            cnt += (N-x)*(x+1)
        elif temp<S:
            for e in range(x+1,N):
                temp += A[e]
                print(temp)
                if temp == S:
                    cnt += (N-e)*(x+1)
                    print("  "+str(cnt))
                    break
                elif temp>S:
                    break
            
    print(cnt)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, S, A)

if __name__ == '__main__':
    main()
