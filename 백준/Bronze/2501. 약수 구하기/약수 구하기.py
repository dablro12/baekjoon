n, k = map(int, input().split())

measure = [] 
for i in range(1, n+1):
    if n%i ==0:
        measure.append(i)

try:
    if n ==1:
        print(1)
    else:
        print(measure[k-1])
except IndexError:
    print(0)
    