n = int(input())
cnt = 1 # 벌집 개수

for i in range(n):
    cnt += i*6
    if n <= cnt: #벌집 개수의 누적이 입력값보다 클때,
        print(i+1)
        break