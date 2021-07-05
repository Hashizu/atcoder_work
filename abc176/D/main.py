#!/usr/bin/env python3
from collections import deque


def main(H,W,CH,CW,DH,DW,m):

    is_serch = [[0]*W for h in range(H)]
    d = [[-1]*W for h in range(H)]

    qs = [deque() for _ in range(H*W)]
    qs[0].append((CH,CW))
    d[CH][CW] = 0

    for i, qq in enumerate(qs):
        while(len(qq)>0):
            th,tw = qq.popleft()
            if is_serch[th][tw]!=1:
                is_serch[th][tw] = 1

                def check_d(tth,ttw, d, qq):
                    if 0<=tth<H and 0<= ttw<W:
                        if m[tth][ttw] == ".":
                            d[tth][ttw] = i
                            if is_serch[tth][ttw]==0:
                                qq.append((tth,ttw))
                
                p = 1
                q = 0
                check_d(th+p,tw+q, d, qq)
                p = 0
                q = 1
                check_d(th+p,tw+q, d, qq)
                p = -1
                q = 0
                check_d(th+p,tw+q, d, qq)
                p = 0
                q = -1
                check_d(th+p,tw+q, d, qq)

                p = 1
                if (d[th+p, tw] == i) or (d[th, tw+p] == i):
                    check_d(th+p, tw+p, d, qq)
                if (d[th-p, tw] == i) or (d[th, tw+p] == i):
                    check_d(th-p, tw+p, d, qq)
                if (d[th+p, tw] == i) or (d[th, tw-p] == i):
                    check_d(th+p, tw-p, d, qq)
                if (d[th-p, tw] == i) or (d[th, tw-p] == i):
                    check_d(th-p, tw-p, d, qq)
                


                def check_m(tth,ttw, d, qq):
                    if 0<=tth<H and 0<= ttw<W:
                        if m[tth][ttw] == ".":
                            d[tth][ttw] = i+1
                            if is_serch[tth][ttw]==0:
                                qs[i].append((tth,ttw))
                p = 2
                q = 0
                check_m(th+p,tw+q, d, qq)
                p = 0
                q = 2
                check_m(th+p,tw+q, d, qq)
                p = -2
                q = 0
                check_m(th+p,tw+q, d, qq)
                p = 0
                q = -2
                check_m(th+p,tw+q, d, qq)

                p = 2
                if (d[th+p, tw] == i+1) or (d[th, tw+p] == i+1):
                    check_m(th+p, tw+p, d, qq)
                if (d[th-p, tw] == i+1) or (d[th, tw+p] == i+1):
                    check_m(th-p, tw+p, d, qq)
                if (d[th+p, tw] == i+1) or (d[th, tw-p] == i+1):
                    check_m(th+p, tw-p, d, qq)
                if (d[th-p, tw] == i+1) or (d[th, tw-p] == i+1):
                    check_m(th-p, tw-p, d, qq)

                # [print(_) for _ in d]
                # print()

    print(d[DH][DW])

    return 1

if __name__ == '__main__':
    H, W = map(int, input().split(" "))
    CH, CW = map(int, input().split(" "))
    DH, DW = map(int, input().split(" "))
    m = [list(input()) for h in range(H)]
    main(H,W,CH-1,CW-1,DH-1,DW-1,m)

# .replace("#", "1").replace(".", "0")