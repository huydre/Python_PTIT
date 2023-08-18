s = input()
cnt = 0
for i in range(0, len(s)) :
    if s[i].islower() : cnt += 1
if cnt >= len(s) - cnt : print(s.lower())
else : print(s.upper())