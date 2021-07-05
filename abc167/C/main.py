#!/usr/bin/env python3
import sys
import numpy as np

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    A = np.zeros((N,M+1))
    for i in range(N):
        A[i] = [int(next(tokens)) for _ in range(M+1)]
    
    min_c = [10000000]

    def dfs(k, dep):
        if dep == N-1:
            if (k[1:]>=X).all():
                min_c[0] = min(min_c[0], k[0])
            elif ((k+A[dep])[1:]>=X).all():
                min_c[0] = min(min_c[0], k[0]+A[dep][0])
        else:
            dfs(k+A[dep],dep+1)
            dfs(k,dep+1)
    
    dfs(np.zeros(M+1), 0)
    
    if min_c[0] != 10000000:
        print(int(min_c[0]))
    else:
        print(-1)




if __name__ == '__main__':
    main()
