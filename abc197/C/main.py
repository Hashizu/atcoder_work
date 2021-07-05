#!/usr/bin/env python3
import sys
import itertools as it


def solve(N: int, A: "List[int]"):
    
    def ORXOR(ps_):
        ps_ = list(ps_)
        prev = 0
        for i, t in enumerate(ps_):
            temp = A[prev]
            for k in range(prev, t):
               temp = temp | A[k]

            prev = t
            
            if i==0:b = temp
            else: b = temp ^ b
        
        temp = A[prev]
        for k in range(ps_[-1],N):
            temp = temp | A[k]
        b = temp^b


        return b
    
    
    ans = A[0]
    for i in A[1:]: ans = ans ^ i
    p = list(range(1,N))
    for i in range(1,N):
        for ps in it.combinations(p, i):
            a = ORXOR(ps)
            ans = min(a,ans)
            if ans==0:
                print(0)
                return
    print(ans)
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