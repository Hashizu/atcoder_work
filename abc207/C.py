import math
N=int(input())
t = [0]*N
l = [0]*N
r = [0]*N

for i in range(N):
    t[i],l[i],r[i]= map(int, input().split())


ans = 0

for p in range(N-1):
    for q in range(p+1, N):
        # p<<q
        if ((t[p]==2) or (t[p]==4)):
            pq = r[p]-1 < l[q]
        else:
            if ((t[q]==3) or (t[q]==4)):
                pq = r[p] <= l[q]
            else:
                pq = r[p] < l[q]
        # q<<p
        if ((t[q]==2) or (t[q]==4)):
            qp = r[q]-1 < l[p]
        else:
            if ((t[p]==3) or (t[p]==4)):
                qp = r[q] <= l[p]
            else:
                qp = r[q] < l[p]

        ans += 1-(pq or qp)*1
print(ans)

