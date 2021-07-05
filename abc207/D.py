import numpy as np
import math
from numpy import linalg as LA
def main():
    N=int(input())

    S = np.zeros((N,2))
    T = np.zeros((N,2))


    for i in range(N):
        S[i,0],S[i,1]= map(int, input().split())
    for i in range(N):
        T[i,0],T[i,1]= map(int, input().split())

    def rotate(r):
        C = np.cos(r)
        S = np.sin(r)
        R_x = np.array(
        [ [C, -S],
            [S, C]]
        )
        return R_x

        
    def tangent_angle(u: np.ndarray, v: np.ndarray):
        i = np.inner(u, v)
        n = LA.norm(u) * LA.norm(v)
        c = i / n
        return (np.arccos(np.clip(c, -1.0, 1.0)))


    S = S - np.mean(S,axis=0)
    T = T - np.mean(T,axis=0)
    # print("$")
    # print(np.lexsort(T.T))
    # print(T)
    T_sorted = np.array([T[i] for i in np.lexsort(T.T)])
    # print(T_sorted)
    # print("$")
    for p in range(N):
        for q in range(N):
            if np.isclose(np.linalg.norm(S[p]),np.linalg.norm(T[q])):
                r = tangent_angle(S[p],T[q])
                S_r = np.dot(rotate(r),S.T).T
                S_new = np.array([S_r[i] for i in np.lexsort(S_r.T)])
                # print(r)
                # print(S.shape)
                # print(rotate(r))
                if np.allclose(S_new, T_sorted):
                    print("Yes")
                    return 
                    
                # print(S_new- T_sorted)
                # print(np.mean(S_new,axis=0))
                # break
            # print(np.linalg.norm(S[p]) ,np.linalg.norm(T[q]))
    print("No")
if __name__ == '__main__':
    main()