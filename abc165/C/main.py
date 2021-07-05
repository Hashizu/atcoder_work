#!/usr/bin/env python3
import sys


def solve(N: int, M: int, Q: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]"):

    def cal_p (l):
        p = 0
        for ai,bi,ci,di in zip(a,b,c,d):
            if l[bi-1]-l[ai-1] == ci:
                p+=di
        return p

    max_p = [0]

    def ser (l, prev, dep):
        if dep == N:
            # print(l)
            return cal_p(l)
        else:
            for i in range(prev, M+1):
                max_p[0] = max(ser(l + [i], i, dep+1), max_p[0])
            return 0
    
    max_p = max(ser([],1,0), max_p[0])
    print(max_p)

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
    Q = int(next(tokens))  # type: int
    a = [int()] * (Q)  # type: "List[int]"
    b = [int()] * (Q)  # type: "List[int]"
    c = [int()] * (Q)  # type: "List[int]"
    d = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, M, Q, a, b, c, d)

if __name__ == '__main__':
    main()