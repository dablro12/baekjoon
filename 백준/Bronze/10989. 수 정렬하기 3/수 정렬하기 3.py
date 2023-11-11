import sys
n = int(sys.stdin.readline().rstrip())
l = [0 for _ in range(10001)]
for i in range(n):
    k = int(sys.stdin.readline().rstrip())
    l[k-1] += 1
for i in range(len(l)):
    if l[i] != 0:
        for j in range(l[i]):
            sys.stdout.write(str(i+1)+'\n')