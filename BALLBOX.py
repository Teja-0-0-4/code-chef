t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    m=k*(k+1)//2
    if n>=m:
        print("YES")
    else:
        print("NO")