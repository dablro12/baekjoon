import sys
input = sys.stdin.readline
x_num, x_denom = map(int, input().split()) #분자, 분모 
y_num, y_denom = map(int, input().split()) #분자, 분모 

def gcd(a,b): # 최대 약분을 구하기 위해 최대공약수 함수 생성
    while a!= 0:
        b = b%a # 1. b = 4 / 2. b = 2 / 3. b = 0
        a,b = b,a  # 1. a =4, b = 6 / 2. a = 2, b = 4 / 4. a = 0, b = 2
    return b

res_num = x_num * y_denom + y_num * x_denom 
res_denom = x_denom * y_denom
max_div = gcd(res_num, res_denom)
res_num = res_num // max_div
res_denom = res_denom // max_div
print(f"{res_num} {res_denom}")