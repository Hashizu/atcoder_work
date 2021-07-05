#!/usr/bin/env python3
import sys
import numpy as np

def solve(H: int, W: int, K: int, S: "np.array"):
    print(H, W, K, S)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int

    A = np.zeros((H,W))
    for x in range(H):
        A[x] = [int(_) for _ in next(tokens)]  # type: "List[int]"
    solve(H, W, K, A)

if __name__ == '__main__':
    main()
