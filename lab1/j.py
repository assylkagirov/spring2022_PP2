s = str(input())
p = s.split()
d=" "


for i in range(len(p)):
    if len(p[i])>=3:
        d+=(p[i]+" ")
        
print(d)