s = str(input())
c = str(input())

d = s.find(c)
f = s.rfind(c)
if d!=f:
    print(d, f)
else:
    print(d)