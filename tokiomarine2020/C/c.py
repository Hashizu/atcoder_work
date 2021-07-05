A = [0,1,0,1]

K = 10
for k in range(K):
  A_ = [0]*len(A)
  for i in range(len(A)):
    for ii in range(len(A)):
      A_[i] += (A[ii]>=abs(i-ii))*1
  A = A_
  if sum(A) == len(A)*len(A):
    continue
  print(k,A)
