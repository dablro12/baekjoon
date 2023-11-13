import sys
input =sys.stdin.readline
n = int(input())
xy = []
for i in range(n):
    x,y = map(int, input().split())
    xy.append([x,y])
xy.sort()
    
for i in range(len(xy)):
    print(f"{xy[i][0]} {xy[i][1]}")
