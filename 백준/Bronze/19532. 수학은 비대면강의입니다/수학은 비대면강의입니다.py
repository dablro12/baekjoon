a,b,c,d,e,f = map(int, input().split())
break_tag = 0
for x_i in range(-999, 1000):
    for y_i in range(-999, 1000):
        if break_tag == 1:
            break
        
        if (a*x_i) + (b*y_i) == c and (d*x_i) + (e*y_i) == f:
            print(f"{x_i} {y_i}")
            break_tag = 1 