#!/usr/bin/env python3
import sys

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()

    N = int(next(tokens))  # type: str
    K = int(next(tokens))  # type: str
    # print(N, K)
    g = set()
    for _ in range(K):
        d = int(next(tokens))
        g = g | set([int(next(tokens)) for i in range(d)])

    print(N - len(g))    

    return


if __name__ == '__main__':
    main()
