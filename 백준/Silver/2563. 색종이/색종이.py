import sys
input = sys.stdin.readline
li = []
n = int(input())
white = [[0 for i in range(100)]for i in range(100)]
for i in range(n):
    x,y = map(int, input().split())
    for x_idx in range(x, x+10):
        for y_idx in range(y, y+10):
            white[x_idx][y_idx] = 1 

cnt = 0
for row in white:
    cnt += row.count(1)
print(cnt)