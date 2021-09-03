import heapq
import numpy as np

n,m = map(int,input().split())
e = [ [] for _ in range(n)]

def dijkstra(s, thr):
    hq = [(0, s)]
    heapq.heapify(hq)
    cost = [float('inf')] * n
    cost[s] = 0 # 開始地点は0
    e_cost = [float('inf')] * n

    while hq:
        c, v = heapq.heappop(hq)
        if (c > cost[v]): continue
        for d, u in e[v] :
            tmp = d + cost[v]
            if u <= thr:
                if tmp < cost[u]:
                    cost[u] = tmp
                    heapq.heappush(hq, (tmp, u))
            else:
                if tmp < e_cost[u]:
                    e_cost[u] = tmp
    return np.minimum(cost, e_cost)
    # return [min(a,b) for a,b in zip(cost, e_cost)]

for _ in range(m):
    a,b,t = map(int,input().split())
    a,b = a-1, b-1
    # print(type(e[a]))
    heapq.heappush(e[a], (t, b))

    # e[a].append((t, b))

ans = 0
for thr in range(0,n):
    for i in range(0,n):
        cost = dijkstra(i, thr)
        # print(cost)
        ans+=np.sum(cost[ cost!= float('inf')]).astype(int)

print(ans)