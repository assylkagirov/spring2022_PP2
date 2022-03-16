x = int(input())

s = []

for i in range(x):
    z=str(input())
    s.append(z)
    
for i in range(x):
    if "gmail.com" in s[i]:
        d=s[i]
        print(d[:-10])