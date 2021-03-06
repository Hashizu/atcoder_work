#!/usr/bin/env python3
import sys

def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]"):

    # bc = [c for b,c in zip(B, C) for b_ in range(b)]
    # print(A+bc)
    # k = sorted(A+bc)[-N:]
    a = [(l, 1) for l in A]
    for x, y in zip(C, B):
        a.append((x,y))

    n = N
    ans = 0
    for x, y in sorted(a, reverse=True):
        if n >= y:
            n -= y
            ans += x*y
        else:
            ans += x*n
            break
    
    print(ans)

    # print(sum(k))
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, A, B, C)

if __name__ == '__main__':
    main()
