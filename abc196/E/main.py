#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]", t: "List[int]", Q: int, x: "List[int]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    t = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        t[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, a, t, Q, x)

if __name__ == '__main__':
    main()