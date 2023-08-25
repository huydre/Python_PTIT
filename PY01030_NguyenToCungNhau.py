import math

n, k = [int(i) for i in input().split()]
start = 10 ** (k - 1)
end = 10 ** k
cnt = 0
for i in range(start, end):
    if math.gcd(n, i) == 1:
        if cnt == 10:
            cnt = 0
            print()
        print(i, end=" ")
        cnt += 1
