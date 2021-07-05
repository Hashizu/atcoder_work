#!/usr/bin/env python3


def main():
    N = int(input())

    A = list(map(int, input().split(" ")) ) # type: "List[int]"
    p = A[:2**(N-1)]
    a = A[2**(N-1):]
    mp = max(p)
    ma = max(a)
    if mp>ma:
        print(2**(N-1)+a.index(ma)+1)
    else:
        print(p.index(mp)+1)

    return 0

if __name__ == '__main__':
    main()
