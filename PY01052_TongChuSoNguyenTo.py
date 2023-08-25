import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def is_valid(n):
    sum = 0
    for i in n :
        sum += int(i)
    return is_prime(sum)


t = int(input())
for p in range(t):
    n = input()
    if is_valid(n):
        print("YES")
    else:
        print("NO")
