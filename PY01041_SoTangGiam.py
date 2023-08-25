def isValid(s):
    if len(s) < 3:
        return False
    ar = list(int(i) for i in s)
    up = True
    for i in range(1, len(ar)):
        if up and ar[i] <= ar[i - 1]:
            up = False
        elif not up and ar[i] >= ar[i - 1]:
            return False
    return True


t = int(input())
for p in range(t):
    n = input()
    if isValid(n):
        print("YES")
    else:
        print("NO")
