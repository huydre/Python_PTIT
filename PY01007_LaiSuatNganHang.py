import math

t = int(input())
for p in range(t) :
    n, x, m = [float(i) for i in input().split()]
    res = math.log(m / n, 1 + x / 100)
    print(math.ceil(res))