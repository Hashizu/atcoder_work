#!/usr/bin/env python3


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N = int(input())
    d = [ input().split(" ") for i in range(N)]
    d = [(int(c),int(x)) for x,c in d]
    print(sorted(d))
if __name__ == '__main__':
    main()
