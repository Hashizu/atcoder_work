#!/usr/bin/env python3
import sys


def solve(X: str):
    print(str(X).split(".")[0])
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = str(next(tokens))  # type: float
    solve(X)

if __name__ == '__main__':
    main()
