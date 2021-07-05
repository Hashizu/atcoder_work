#!/usr/bin/env python3
import sys

t  = [0,1,2,3,4,5,6,7,8,9]
tb = [0,7,0,9,0,0,0,1,0,3]

def solve(K: int):
    k =K
    temp = 0
    ct = 0
    b = k%10

    while(True):
        ct+=1
        u = temp%10
        p = -1
        for i in range(10):
            if (u + (b*i)) %10 == 7:
                p = i
                break
        if p == -1:
            print(-1)
            return
        temp += k*p
        if temp == 7:
            print(ct)
            return
        temp //= 10

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)

if __name__ == '__main__':
    main()