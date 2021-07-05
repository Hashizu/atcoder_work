#!/usr/bin/env python3
import sys
import math


def solve(A: int, B: int):
    
    kmina = math.ceil((A)/0.08)
    kmaxa = (A + 1)/0.08
    
    kminb = math.ceil((B)/0.10)
    kmaxb = (B + 1)/0.10
    
    if (kmina <= kminb) and (kminb < kmaxa):
        print(kminb)    
    elif (kminb <= kmina) and (kmina < kmaxb):
        print(kmina)
    else:
        print(-1)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
