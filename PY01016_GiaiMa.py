t = int(input())
for p in range(t) :
    s = input()
    for i in range (0, len(s)) :
        if (s[i].isalpha()) :
            for j in range(int(s[i+1])) : print(s[i],end = "")
    print()