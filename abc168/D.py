from heapq import heapify, heappop, heappush

def dijkstra(start,node,edge):
    d = [2*10**5] * node
    m = [0]*node
    d[start] = 0
    q = [(0,0)]
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

def main():
    N,M = map(int, input().split())
    
    E = [[] for _ in [0]*N]
    for i in range(M):
      a,b = (int(x) for x in input().split())
      E[a-1].append(b-1)
      E[b-1].append(a-1)

    m = dijkstra(0, N, E)
    print("Yes")
    print("\n".join(map(str, m[1:])))

if __name__ == '__main__':
    main()
