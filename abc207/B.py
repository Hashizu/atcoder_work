import math
A, B, C, D= map(int, input().split())

b = C*D-B
if b<=0 :
    print(-1)
else:
    print(math.ceil(A/b))