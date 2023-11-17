import sys
input =sys.stdin.readline
a,b = map(int, input().split()) #최초 a = 6 , b= 10
A,B = a,b #
while a!= 0:
    b = b%a # 1. b = 4 / 2. b = 2 / 3. b = 0
    a,b = b,a  # 1. a =4, b = 6 / 2. a = 2, b = 4 / 4. a = 0, b = 2 
print(A*B // b) # 6*10 // 최종 b : 2