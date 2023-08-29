def sang_nguyen_to(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes


p = sang_nguyen_to(505)


def is_valid(n):
    for i in range(0, len(n)):
        if p[i] and i != '2' and i != '3' and i != '5' and i != '7':
            return "NO"
    return "YES"


for t in range(int(input())):
    n = input()
    # print(is_valid(n))
    for i in range(0, len(p)) :
        print(p[i])
