n = int(input())
div = 2
tmp = []
while True:
    if n == 1:
        break
    else:
        if n % div == 0:
            n = n / div
            tmp.append(div)
        else:
            div += 1
    
for i in tmp:
    print(i)