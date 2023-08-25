import math


def reverse(n):
    rev = 0
    while n > 0:
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    return rev


t = int(input())
for p in range(t):
    n = int(input())
    rev = reverse(n)
    if math.gcd(n, rev) == 1:
        print("YES")
    else:
        print("NO")
