import math


def is_valid(s):
    rev = s[::-1]
    for i in range(0, len(s) - 1):
        if math.fabs(int(ord(s[i + 1]) - ord(s[i]))) != math.fabs(int(ord(rev[i + 1])) - ord(rev[i])):
            return "NO"
    return "YES"


for t in range(int(input())):
    s = input()
    print(is_valid(s))
