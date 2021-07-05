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



def solve(n: int, a: int, b: int):
    k = pow(2, n, MOD) - combination(n,a) - combination(n,b)
    print(k % MOD - 1)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(n, a, b)

if __name__ == '__main__':
    main()
