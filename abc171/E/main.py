#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    all_a = a[0]
    for ai in a[1:]:
        all_a = all_a ^ ai
    ans = []
    for ai in a:
        ans.append(all_a^ai)
    print(*ans)
    
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
