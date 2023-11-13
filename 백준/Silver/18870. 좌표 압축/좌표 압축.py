import sys
input =sys.stdin.readline
n = int(input())
x_li = list(map(int, input().split()))
# x_li = '2 4 -10 4 -9'.split()
# x_li = '1000 999 1000 999 1000 999'.split()
x_sort = list(set(x_li))
x_sort.sort()

num_dict= {}
for i in range(len(x_sort)):
    num_dict[x_sort[i]] = i 
for i in x_li:
    print(num_dict[i], end = ' ')