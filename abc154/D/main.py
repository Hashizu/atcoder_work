#!/usr/bin/env python3
import sys


def solve(N: int, K: int, p: "List[int]"):
    p = [(p_ +1)/2 for p_ in p]
    temp = sum(p[0:K])
    max_s = temp

    for i in range(K, N):
        temp = temp - p[i-K] + p[i]
        max_s = max(max_s, temp)
    
    print(max_s)




    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, p)

if __name__ == '__main__':
    main()
