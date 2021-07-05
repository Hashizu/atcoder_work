#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: str):
    a = 0
    for n in N:
        a+=int(n)
        a%=9
    if a==0:print(YES)
    else:print(NO)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = next(tokens)  # type: str
    solve(N)

if __name__ == '__main__':
    main()
