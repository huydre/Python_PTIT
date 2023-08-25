def is_valid(n):
    for i in n:
        if i != '2' and i != '4' and i != '6' and i != '8' and i != '0' : return False
    return True


t = int(input())
for p in range(t):
    n = int(input())
    for i in range(22,n,2) :
        j = str(i)
        if is_valid(j) and j == j[::-1] and len(j) % 2 == 0:
            print(i, end=" ")
    print()
