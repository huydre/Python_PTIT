import math
import functools


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


t = int(input())
for p in range(t) :
    a, b = [int(i) for i in input().split()]
    if is_prime(sum(int(i) for i in str(math.gcd(a, b)))):
        print('YES')
    else:
        print('NO')

