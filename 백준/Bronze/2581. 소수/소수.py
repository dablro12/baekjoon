tmp = []
min_ = int(input())
max_ = int(input())
for num in range(min_, max_+1):
    cnt = 0
    if num>1:
        for i in range(2, num):
            if num % i == 0:
                cnt+=1
        if cnt ==0:
            tmp.append(num)
            
            
if tmp == []:
    print(-1)
else:
    print(sum(tmp))
    print(tmp[0])