import math
t = input().split(" ")
A, B, H, M = [int(te) for te in t]

mins = H * 60 + M

l = mins * 0.5
s = M * 6

c2 = A*A + B*B - 2*A*B*math.cos(math.radians(abs(l-s)))

print(pow(c2,0.5))