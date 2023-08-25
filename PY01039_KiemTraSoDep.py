def isValid(n):
    unique = set(n)
    if len(unique) != 2: return False
    for i in range(0, len(n) - 2):
        if n[i] != n[i + 2]: return False
    return True


t = int(input())
for p in range(t):
    n = input()
    if isValid(n):
        print("YES")
    else:
        print("NO")
