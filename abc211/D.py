from collections import deque

class Node:
    def __init__(self, num):
        self.num = num
        self.edge = []
        self.dist = N*2
        self.keiro = 0
        self.is_ser = 0
    
    def set_dist(self, dist_):
        self.dist = dist_
    
    def set_edge(self, e):
        self.edge.append(e)

    def remove_edge(self, e):
        self.edge.remove(e)

    def set_keiro(self, e):
        self.keiro = e

    def set_ser(self, e):
        self.is_ser = e

N,M = map(int, input().split(" "))

nodes = [Node(num+1) for num in range(N)]

for i in range(M):
    a,b = map(int, input().split(" "))
    nodes[a-1].set_edge(b-1)
    nodes[b-1].set_edge(a-1)

nodes[0].set_dist(0)
nodes[0].set_keiro(1)
nodes[0].set_ser(1)


d = deque()
d.append(nodes[0])

on_d = [0]*N
on_d[0] = 1

while d:
    v = d.popleft()
    # on_d[v.num] = 1
    # print(v.edge)
    for v_ in v.edge:
        if nodes[v_].is_ser==1:
            continue
        # print(nodes[v_].dist , v.dist+1)
        if nodes[v_].dist > v.dist+1:
            nodes[v_].set_dist(v.dist+1)
            nodes[v_].set_keiro(v.keiro)
            d.append(nodes[v_])
        elif nodes[v_].dist == v.dist+1:
            nodes[v_].set_keiro(v.keiro + nodes[v_].keiro)
            d.append(nodes[v_])
    print("dist {}".format([k.dist for k in nodes]))
    print("keiro {}".format([k.keiro for k in nodes]))

    v.set_ser(1)

print("keiro {}".format([k.keiro for k in nodes]))
print("keiro {}".format([k.is_ser for k in nodes]))
print(nodes[N-1].keiro)
