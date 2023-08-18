import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


t = int(input())

for p in range(t):
    n = int(input())
    cnt = 0
    for i in range(1,n+1,1) :
        if math.gcd(i,n) == 1 : cnt = cnt + 1
    if (is_prime(cnt)) : print("YES")
    else : print("NO")