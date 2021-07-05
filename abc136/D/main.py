#!/usr/bin/env python3
import sys

def solve(S: str):
    prev = -1
    ans = [0] * len(S)
    cr = 0
    cl = 0
    for i, x in enumerate(S):
        if x == "R":
            if prev == "L":
                # print("cr {} cl {}".format(cr, cl))
                ans[prev_R] = cr//2 + cl//2 + cr%2
                ans[prev_L] = cr//2 + cl//2 + cl%2
                cr = 0
            prev_R = i
            cr += 1
        elif x == "L":
            if prev == "R":
                cl = 0
                prev_L = i
            cl += 1
        # print(ans)
        prev = x
    
    ans[prev_R] = cr//2 + cl//2 + cr%2
    ans[prev_L] = cr//2 + cl//2 + cl%2

    print(*ans)

    
    
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()