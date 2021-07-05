#!/usr/bin/env python3
import sys
MOD = 1000000007  # type: int

def combination(n: int, r:int, mod=MOD):
    n1 = n+1
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod

def solve(X: int, Y: int):

    u = (2*Y - X)//3
    r = (X- u)//2

    if ((2*Y - X)%3!=0) or (r*u <0):
        print(0)
        return

    a = combination(u+r, u)
    print(a)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(X, Y)

if __name__ == '__main__':
    main()
