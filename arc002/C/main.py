#!/usr/bin/env python3


def main():

    N = int(input())
    C = input()

    bt = ["A","B","X","Y"]
    st = [x+y for x in bt for y in bt]
    min_l = N

    for l in st:
        for r in st:
            i = 0
            length = N
            while(i < N):
                if C[i:i+2] in (l,r):
                    i+=1
                    length-=1
                i+=1
            min_l = min(min_l, length)
    print(min_l)
    return

if __name__ == '__main__':
    main()
