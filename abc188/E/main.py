#!/usr/bin/env python3

class UnionFind:
    """
    同じ親を持つ場合は木を統合し続け，
    独立したネットワークの数が親の数になる木
    parはrootによって更新しなければならない
    (parに直接アクセスしない)
    """
    def __init__(self, num):
        self.par = list(range(1,num+1))
        self.size = [1]*num
    
    def root(self, n):
        if self.par[n-1] != n:
            self.par[n-1] = self.root(self.par[n-1])
        return self.par[n-1]

    def unite(self, a, b):
        a=self.root(a)
        b=self.root(b)
        if a!=b:
            self.par[b-1]=a
            self.size[a-1] += self.size[b-1]
        return
    
    def get_size(self, n):
        return self.size[self.root(n)-1]

def main():
    N,M = map(int, input().split(" "))
    A = map(int, input().split(" "))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i],Y[i] = map(int, input().split(" "))


    union = UnionFind(N)
    for i in range(M):
        union.unite(X[i],Y[i])
    for i in range(N):print(union.root(i))
    

if __name__ == '__main__':
    main()
