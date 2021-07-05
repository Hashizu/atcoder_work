#!/usr/bin/env python3


def main(N,A):
    pre=0
    max_d = 0
    max_pre = 0
    cur = 0

    for ai in A:
        pre += ai
        max_pre = max(max_pre,pre)
        max_d = max(max_d,cur+max_pre)
        cur += pre
        max_d = max(max_d,cur)

    print(max_d)

    return

if __name__ == '__main__':
    def load_input():
        N = int(input())
        A = list(map(int, input().split(" ")))
        return N,A
    N,A=load_input()
    main(N,A)
