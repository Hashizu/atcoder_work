A, B, C= map(int, input().split())

c_ = C % 2

if C==0:
    print("=")

elif c_ == 0 :
    if abs(A)==abs(B):
        print("=")
    elif abs(A)<abs(B):
        print("<")
    else:
        print(">")

elif c_ != 0 :
    if A<B:
        print("<")
    elif A>B:
        print(">")
    else:
        print("=")
        