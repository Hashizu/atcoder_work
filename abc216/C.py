N=int(input())
t=str(bin(N))[2:]
print(t.replace("0","B").replace("1","BA"))