def is_valid(a, b):
    a.sort()
    b.sort()
    for i in range(0, len(a)):
        if (a[i] > b[i]): return "NO"
    return "YES"


for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print(is_valid(a,b))