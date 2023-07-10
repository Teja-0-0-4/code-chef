t=int(input())
for i in range(t):
    A,B,C,D=map(int,input().split())
    if A<B:
        A=A+C
        if A<B:
            A=A+D
        else:
            B=B+D
    else:
        B=B+C
        if B<A:
            B=B+D
        else:
            A=A+D
    if A<B:
        print("S")
    else:
        print("N")