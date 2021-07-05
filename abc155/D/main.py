#!/usr/bin/env python3
import sys

# https://atcoder.jp/contests/abc155/submissions/12182341
def main(N, K, Ap, Am):
    p = len(Ap)
    m = len(Am)
    Ap.sort()
    Am.sort(reverse=True)
    U = 10 ** 18
    L = - 10 ** 18

    while U - L > 1:
        # print("U: {}  L:{}".format(U, L))
        mid = (U+L)//2
        cnt = 0
        if mid >= 0:
            cnt += p*m
            i = p
            t = 0
            for a in Ap:
                while i and Ap[i-1] * a > mid: i -= 1
                t += i
                if a*a <= mid: t -= 1
            cnt += t//2
            i = m
            t = 0
            for a in Am:
                while i and Am[i-1] * a > mid: i -= 1
                t += i
                if a*a <= mid: t -= 1
            cnt += t//2
        else:
            i = m
            for a in Ap:
                while i and Am[i-1] * a <= mid: i -= 1
                cnt += m - i   
        
        if cnt < K:
            L = mid
        else:
            U = mid
        # print("after U: {}  L:{}".format(U, L))
    
    print(U)


    return

if __name__ == '__main__':
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    Ap = []
    Am = []
    # A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    for _ in range(N):
        t = int(next(tokens))
        if t>=0:
            Ap.append(t)
        elif t<0:
            Am.append(t)
    main(N, K, Ap, Am)
