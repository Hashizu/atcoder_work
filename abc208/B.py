P = int(input())
def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)
a = 0
p = P
for i in range(10,0, -1):
    c = p // fact(i)
    a += c
    p -= fact(i)*c

print(a)