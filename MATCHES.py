for i in range(int(input())):
    c = 0
    a, b = map(int,input().split())
    summ = a + b
    s = str(summ)
    for i in range(len(s)):
        if s[i] == '0' or s[i] == '6' or s[i] == '9':
            c += 6
        elif s[i] == '1':
            c += 2
        elif s[i] == '2' or s[i] == '3' or s[i] == '5':
            c += 5
        elif s[i] == '4':
            c += 4
        elif s[i] == '8':
            c += 7
        elif s[i] == '7':
            c += 3
    print(c)