a = str(input())
pelin = a[::-1]
tmp = int(len(a)/2) 
for i in range(tmp):
    if pelin[i] == a[i]:
        tmp -= 1
if tmp ==0:
    print(1)
else:
    print(0)