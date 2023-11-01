x = int(input())
tup = (25, 10, 5, 1)
for _ in range(x):
    money = int(input())
    for i in tup:
        print(int(money//i), end=' ')
        money %= i