P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    a = input()
    if a == '0' : break
    k,s = a.split()
    k = int(k)
    str = ""
    for i in s:
        str += P[(P.find(i) + k) % 28]
    print(str[::-1])
