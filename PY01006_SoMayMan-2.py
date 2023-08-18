def luckyNumber(n) :
    for i in range(0,len(n)) :
        if n[i] != "4" and n[i] != "7" : return "NO"
    return "YES"


t = int(input())
for p in range(t) :
    n = input()
    print(luckyNumber(n))