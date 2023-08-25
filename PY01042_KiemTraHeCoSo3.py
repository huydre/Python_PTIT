def is_valid(s):
    for i in s:
        if i != '0' and i != '1' and i != '2': return "NO"
    return "YES"


t = int(input())
for p in range(t):
    s = input()
    print(is_valid(s))