t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    a= (l[0]**2)/(l[2]**3)
    b= (l[1]**2)/(l[3]**3)
    if a==b:
        print("Yes")
    else:
        print("NO")