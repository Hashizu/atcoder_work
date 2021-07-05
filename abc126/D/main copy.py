#!/usr/bin/env python3
import sys

class Node:
    def __init__(self, n, N):
        self.id = n
        self.edges = []
        self.weights = [-1]*N
        self.color = 1
        self.s = 0
    def set_edge(self, e, w):
        self.edges.append(e)
        self.weights[e]=w
    def set_color(self, c_):
        self.color = c_
        self.s = 1

def solve(N: int, u: "List[int]", v: "List[int]", w: "List[int]"):

    # init nodes
    nodes = [Node(i,N) for i in range(N)]
    # set edges
    for ui, vi, wi in zip(u, v, w):
        nodes[ui-1].set_edge(vi-1,wi)
        nodes[vi-1].set_edge(ui-1,wi)

    def cal(node):
        c_ = node.color
        for n in node.edges:
            if nodes[n].s == 0:
                if node.weights[n]%2==1:
                    nodes[n].set_color(c_*-1)
                else:
                    nodes[n].set_color(c_)                
                cal(nodes[n])
    
    cal(nodes[0])

    for n in nodes:
        print((n.color==1)*1)

    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    w = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, u, v, w)

if __name__ == '__main__':
    main()