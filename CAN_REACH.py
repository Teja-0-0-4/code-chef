t=int(input())
for i in range(t):
    A,B,C=map(int,input().split())
    if A<0:
        A=abs(A)
    elif B<0:
        B=abs(B)
    if A%C==0 and B%C==0:
        print("YES")
    else:
        print("NO")