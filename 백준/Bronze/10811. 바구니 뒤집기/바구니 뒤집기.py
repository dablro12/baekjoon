import sys
input =sys.stdin.readline
n,m = map(int, input().split())
li = [_+1 for _ in range(n)]
for _ in range(m):
    i,j = map(int, input().split())
    tmp_li = li[i-1:j]
    tmp_li.reverse()
    li[i-1:j] = tmp_li
for _ in li:
    print(f"{_}", end=' ')