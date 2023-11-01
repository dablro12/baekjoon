n,b = map(str, input().split())
b= int(b)
#int(string, base)
to_ten = 0
for i in range(len(n)):
    n_zin = int((n[i]), b)
    tmp = n_zin*(b **(len(n)-i-1))
    to_ten += tmp
    
print(to_ten)