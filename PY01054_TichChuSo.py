t = int(input())
for p in range(t):
    n = input()
    res = 1
    for i in n :
        if i != '0': res *= int(i)
    print(res)