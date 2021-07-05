#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    a = sorted(A)
    asum = [0]*N
    asum[0]=a[0]
    for x in range(1, N):
        asum[x] = asum[x-1]+a[x]
    
    stop = -1
    for i in range(N-1):
        if asum[i] * 2 < a[i+1]:
            stop = i
    print(N-stop-1)


    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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
