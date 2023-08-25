def is_valid(s):
    if (len(s) % 2 == 0 or s[0] == s[1]) : return "NO"
    for i in range(0,len(s),2) :
        if (s[i] != s[0]) : return "NO"
    return "YES"

t = int(input())
for p in range(t):
    s = input()
    print(is_valid(s))