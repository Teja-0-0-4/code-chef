t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if k==0:
        if n%4==0:
            print("Off")
        else:
            print("On")
    elif k==1:
        if n%4==0:
            print("On")
        else:
            print("Ambiguous")