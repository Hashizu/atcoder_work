X = input()

if len(set(X))==1:
    print("Weak")
else:
    is_w= 1
    for i in range(1,4):
        if (int(X[i-1])+1)%10 == int(X[i]):
            is_w*=1
        else:
            is_w=0
    if is_w != 1:
        print("Strong")
    else:print("Weak")
