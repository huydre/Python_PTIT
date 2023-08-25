def is_divisible_3(n):
    sum = 0
    for i in n :
        sum += int(i)
    return sum % 3 == 0

t = int(input())
for p in range(t) :
    n = input()
    if (is_divisible_3(n)) : print("YES")
    else : print("NO")