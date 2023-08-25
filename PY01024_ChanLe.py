def result(n) :
    cnt = int(n[0])
    for i in range(1,len(n)) :
        if abs(int(n[i]) - int(n[i-1])) != 2 : return False
        cnt += int(n[i])
    if (cnt % 10 == 0) : return True
    return False

for p in range(int(input())) :
    n = input()
    if (result(n)) : print("YES")
    else : print("NO")