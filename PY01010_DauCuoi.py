t = int(input())

for p in range(t) :
    n = input()
    first = slice(0,2)
    last = slice(len(n)-2,len(n))
    if (n[first] == n[last]) : print("YES")
    else : print("NO")