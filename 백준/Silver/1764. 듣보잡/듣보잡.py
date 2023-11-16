import sys
input =sys.stdin.readline
n, m = map(int,input().split())
no_heard, no_saw = [], []

for _ in range(n):
    name = input().strip()
    no_heard.append(name)
for _ in range(m):
    name = input().strip()
    no_saw.append(name)

and_operator = set(no_heard) & set(no_saw)

print(len(set(and_operator)))
for _ in sorted(and_operator):
    print(_)