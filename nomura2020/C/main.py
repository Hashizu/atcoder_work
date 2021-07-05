#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    if N==0:
        if A[0] == 1:
            print(1)
        else:
            print(-1) 
        return 
    
    s = [0]*(N+1)
    s[N] = A[N]
    for i in range(N-1, -1, -1):
        s[i] = s[i+1] + A[i] 

    leafs = 0
    ans = 0
    for i, a in enumerate(A):
        leafs = leafs*2 + a
        rem = pow(2,i) - leafs
        if i<N:
            # print(sum(A[i+1:]), s[i+1])
            k = min(rem, s[i+1])
            ans+=k
    # print(leafs)

    rem = pow(2,N) - leafs    
    if rem<0:
        print(-1)
        return
    print(ans+sum(A))
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N - 0 + 1)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()