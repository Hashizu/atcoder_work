#!/usr/bin/env python3
import sys
def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)

def n_lcd(a,b):
    return a*b//gcd(a,b)

# lcd of a1*x1+n1 & a2*x2+n2
def lcd(a1, n1, a2, n2, M):
    # if a1*a2 == 0:
        # return M, M
    x1 = 0
    x2 = 0
    k1 = n1
    k2 = n2
    while (k1 != k2)&(k1<M+2)&(k2<M+2):
        if k1 < k2:
            x1 += max(1,(k2-k1)//a1)
            k1 = a1*x1 + n1
        else:
            x2 += max(1, (k1-k2)//a2)
            k2 = a2*x2 + n2
        # print(k1, k2)
    return k1, n_lcd(a1, a2)


def solve(N: int, M: int, a: "List[int]"):
    a = (list(set(a)))
    base = 1
    base_n = 0
    for i in a:        
        base_n, base = lcd(base, base_n, i, i//2, M)
        if base >= M:
            print(0)
            return 

    if base > M:
        print(0)
    else:
        print((M-base_n)//base + 1)

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
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, a)

if __name__ == '__main__':
    main()
