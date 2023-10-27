import sys
input =sys.stdin.readline
n,m = map(int, input().split())
li =[i for i in range(1,n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    tmp = li[i-1]
    li[i-1] = li[j-1]
    li[j-1] = tmp
for _ in li:
    print(f"{_}", end=' ')