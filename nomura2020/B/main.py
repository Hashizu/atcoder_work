#!/usr/bin/env python3
import sys


def solve(T: str):
    a = ""
    # prev = ""
    for i in range(len(T)):
        t = T[i]
        if t == "?":
            t="D"
        a+=t
        # prev = t
    print(a)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    T = next(tokens)  # type: str
    solve(T)

if __name__ == '__main__':
    main()
