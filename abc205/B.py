N= int(input())
A= list(map(int, input().split()))

print("Yes" if sorted(A) == list(range(1,N+1)) else "No")