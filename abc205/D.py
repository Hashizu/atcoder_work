import bisect


N, Q= map(int, input().split())
A = list(map(int, input().split()))
K = [0] * Q
J = [-1] * N # すぐ左のK以外の数が何番目の数か

for q in range(Q):
  K[q] = int(input())

J[0] = A[0]-1
for q in range(1, N):
  J[q] = J[q-1] + (A[q] - A[q-1] - 1)

for q in range(Q):
  b_ = bisect.bisect_left(J,K[q])
#   print(b_)
  if b_ == len(A):
    print(A[b_-1] + (K[q] - J[b_-1]))
  else:
    # print(A[b_] ,(J[b_] , K[q]))
    print(A[b_] - 1 - (J[b_] - K[q]))
    # print("dsdf")