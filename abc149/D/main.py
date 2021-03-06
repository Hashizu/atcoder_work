#!/usr/bin/env python3
import sys



def solve(N: int, K: int, R: int, S: int, P: int, T: str):

    T = [int(t_) for t_ in T.replace("r","0").replace("s","1").replace("p","2")]
    # win = (h-1) % 3
    r = 0
    s = 1
    p = 2 
    PS = (R,S,P)
    pt = 0
    for k in range(K):
        pre_ = 3
        for c_ind in range(k, len(T), K):
            c_ = T[c_ind]
            if c_ != pre_:
                pt +=  PS[(c_-1)%3]
                pre_ = c_
            else:
                pre_ = 3
    print(pt)



    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    T = next(tokens)  # type: str
    solve(N, K, R, S, P, T)

if __name__ == '__main__':
    main()
