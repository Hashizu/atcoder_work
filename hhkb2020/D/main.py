#!/usr/bin/env python3

MOD = 1000000007  # type: int


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    T = int(input())
    for i in range(T):
        N, A, B = input().split(" ")
        a = 0
        # 1
        if (N-A-B) > 0:
            a+= (N-A-B+1)**2
        # 2
        


if __name__ == '__main__':
    main()