#!/usr/bin/env python3
import sys
import numpy as np


def solve(N: int, C: int, a: "List[int]", b: "List[int]"):
    k = sorted(a+b)
    res = 0
    pp = 0 # pay on day
    old_d = 0
    # print(k)
    l = len(k)
    i = 0
    while(i<l):
        (td,tp) = k[i]
        if pp < C: res += pp*(td-old_d)
        else:      res += C *(td-old_d)
        # print(td,pp,res)
        pp += tp
        i+=1
        while (i<l) and (td==k[i][0]):
            pp += k[i][1]
            i+=1
        old_d = td
    # print(td,pp,res)

    print(res)

    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    a = [(int(),int())] * (N)  # type: "List[int]"
    b = [(int(),int())] * (N)  # type: "List[int]"
    # c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a_ = int(next(tokens))
        b_ = int(next(tokens))
        c_ = int(next(tokens))
        a[i] = (a_,c_)
        b[i] = (b_+1,-c_)

        

    solve(N, C, a, b)

if __name__ == '__main__':
    main()
