def result(s):
    revs = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(revs[i]) - ord(revs[i-1])):
            return False
    return True


t = int(input())
for p in range(t):
    s = input()
    if result(s) : print("YES")
    else : print("NO")

