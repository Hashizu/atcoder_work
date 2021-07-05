from heapq import heapify, heappop, heappush
from collections import deque
import sys
sys.setrecursionlimit(1000000)

MOD = 1000000007  # type: int

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


def dijkstra(start,node,edge):
    d = [2*10**5] * node
    m = [0]*node
    d[start] = 0
    q = [(d[start],start)]
    heapify(q)
    
    while(len(q) != 0):
      ci, i = heappop(q)
      di = d[i]
      for j in edge[i]:
        if(d[j] > di+1):
          d[j] = di + 1
          heappush(q, (di+1,j))
          m[j] = i+1
    return m

##########################################
MAX = 600000
fac = [0] * MAX
ifac = [0] * MAX
fac[0] = 1
for i in range(1,MAX):
    fac[i] = (fac[i-1] * i) % MOD
ifac[MAX-1] = pow(fac[MAX-1],MOD-2,MOD)
for i in reversed(range(1,MAX)):
    ifac[i-1] = (ifac[i] * i) % MOD
 def combination(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return (fac[n] * ifac[k] * ifac[n-k]) % MOD

##########################################

def combination(n: int, r:int, mod=MOD):
    n1 = n+1
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod

##########################################

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

##########################################

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort()
    return divisors

def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)


def load_input():
    N = int(input())
    A = list(map(int, input().split(" ")))
