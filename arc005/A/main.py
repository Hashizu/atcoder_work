#!/usr/bin/env python3
import sys


def solve(N: int, w: "List[str]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    w = [next(tokens) for _ in range(N - 1 - 0 + 1)]  # type: "List[str]"
    solve(N, w)

if __name__ == '__main__':
    main()
