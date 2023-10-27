import sys
input = sys.stdin.readline
n = int(input())
n_li = input().split(' ')
v = int(input())
cnt = 0
for n in n_li:
    if int(n) == v:
        cnt+=1
print(cnt)
    