t = int(input())
for p in range(t) :
    n = int(input())
    sum = 0
    if n % 2 :
        for i in range(1,n+1,2) : sum += 1/i
    else :
        for i in range(2,n+1,2) : sum += 1/i
    sum = round(sum,6)
    sum = "{:.6f}".format(sum)
    print(sum)