#!/usr/bin/env python3
import sys
def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)

def solve(N: int, M: int, a: "List[int]"):
    a = [t//2 for t in list(set(a))]

    g = a[0]
    for t in a:
        g = gcd(g, t)

    ag = [t//g for t in a] 

    mu = 1
    for t in ag:
        if t%2==1:
            mu*= t//gcd(t,mu)
        else:
            print(0)
            return
    # print(g)
    # print(mu)
    print((M//(mu*g)+1)//2)



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
