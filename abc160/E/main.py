#!/usr/bin/env python3
import sys
from collections import deque


def solve(X: int, Y: int, A: int, B: int, C: int, p: "List[int]", q: "List[int]", r: "List[int]"):

    a=deque(sorted(p)[-X:])
    b=deque(sorted(q)[-Y:])
    c=deque(sorted(r))


    # print("a : {}".format(a))
    # print("b : {}".format(b))
    # print("c : {}".format(c))

    a_min = a.popleft()
    b_min = b.popleft()

    a_temp = a_min
    b_temp = b_min
    ans = 0
    
    while(len(c)>0):
        c_temp = c.pop()
        is_cand_a = (a_min < c_temp) & (a_temp !=0)
        is_cand_b = (b_min < c_temp) & (b_temp !=0)
        
        if is_cand_a & is_cand_b:
            if a_temp < b_temp:
                if len(a)>0:
                    a_temp = a.popleft()
                else:
                    a_temp = 0
            else:
                if len(b)>0:
                    b_temp = b.popleft()
                else:
                    b_temp = 0
        elif is_cand_a:
            if len(a)>0:
                a_temp = a.popleft()
            else:
                a_temp = 0
        elif is_cand_b:
            if len(b)>0:
                b_temp = b.popleft()
            else:
                b_temp = 0
        else:
            break

        if is_cand_a | is_cand_b:
            # print("ans:{} c_temp: {}".format(ans, c_temp))
            ans += c_temp

    ans += sum(a)+sum(b)+a_temp+b_temp
    print(ans)



    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(A)]  # type: "List[int]"
    q = [int(next(tokens)) for _ in range(B)]  # type: "List[int]"
    r = [int(next(tokens)) for _ in range(C)]  # type: "List[int]"
    solve(X, Y, A, B, C, p, q, r)

if __name__ == '__main__':
    main()