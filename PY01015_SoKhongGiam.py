def soKhongGiam(n) :
    for i in range(0,len(n)-1) :
        if n[i] > n[i+1] : return False
    return True


t = int(input())
for p in range(t) :
    n = input()
    if soKhongGiam(n) : print("YES")
    else : print("NO")