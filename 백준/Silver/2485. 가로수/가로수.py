# 이미 심어진 가로수 수
import sys
input = sys.stdin.readline
n = int(input())
# 첫 가로수 위치
a = int(input())

# 가로수 사이 저장 배열
arr = []

#gcb 최소 공약수 알고리즘
def gcd(a,b):
    while a != 0:
        b = b%a
        a,b= b,a
    return b
# 가로수들 사이 간격 저장
for i in range(n-1):
    num = int(input())
    arr.append(num -a)
    a = num

g = arr[0]
for j in range(1, len(arr)):
    g= gcd(g, arr[j])
result = 0
for each in arr:
    result += each//g - 1
print(result)