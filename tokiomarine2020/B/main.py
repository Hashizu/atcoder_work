#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(A: int, V: int, B: int, W: int, T: int):
    
    d_dif = abs(A-B)
    if d_dif==0:
        print(YES)
        return
    v_dif = V - W
    if v_dif <=0:
        print(NO)
        return
    t = d_dif/v_dif
    if t <= T:
        print(YES)
    else:
        print(NO)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    V = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    solve(A, V, B, W, T)

if __name__ == '__main__':
    main()