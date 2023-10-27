import sys 
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split(' ')))
li.sort()
print(f"{li[0]} {li[-1]}")