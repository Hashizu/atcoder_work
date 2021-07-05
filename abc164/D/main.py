#!/usr/bin/env python3
import sys


def solve(S: int):
    S =str(S)[::-1]
    MOD = 2019
    mod_l = [int(0)]*2019
    mod_l[0] = 1
    prev = 0
    for x in range(len(S)):
        k = int(S[x]) * pow(10, x, MOD) % MOD + prev
        mod_l[k%2019] += 1
        prev = k%2019

    s = sum([x*(x-1)//2 for x in mod_l])
    print(s)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = int(next(tokens))  # type: int
    solve(S)

if __name__ == '__main__':
    main()