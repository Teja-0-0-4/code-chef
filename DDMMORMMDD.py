t=int(input())
for i in range(t):
    s=input()
    if s[0:2]<="31" and s[3:5]<="12" and s[0:2]<="12" and s[3:5]<="31":
        print("BOTH")
    elif s[0:2]<="12" and s[3:5]<="31":
        print("MM/DD/YYYY")
    else:
        print("DD/MM/YYYY")
        