k = []

for i in range(4):
    k.append(str(input()))


if set(k) == set(["H" , "2B" , "3B" , "HR"]):
    print("Yes")
else:
    print("No")