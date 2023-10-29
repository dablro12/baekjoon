orig = [1, 1, 2, 2, 2, 8]
pre = str(input()).split()
for i in range(len(orig)):
    print(orig[i] - int(pre[i]), end = " ")