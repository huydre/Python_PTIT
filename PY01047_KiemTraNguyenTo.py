import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def isValid(n):
    n = n[len(n) - 4: len(n)]
    return is_prime(int(n))


t = int(input())
for p in range(t):
    n = input()
    if isValid(n):
        print("YES")
    else:
        print("NO")
