import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def is_valid(n):
    if not is_prime(len(n)): return False
    cnt = 0;
    for i in n :
        if is_prime(int(i)) : cnt += 1
    return cnt > len(n) - cnt


t = int(input())
for p in range(t):
    n = input()
    if is_valid(n):
        print("YES")
    else:
        print("NO")
