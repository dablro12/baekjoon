import sys
input = sys.stdin.readline
n,m = map(int, input().split())
li = [0 for i in range(n)]
for i in range(m):
    i,j,k = map(int, input().split())
    for _ in range(j-(i-1)):
        li[_+(i-1)] = k

for _ in li:
    print(f"{_}", end=' ')