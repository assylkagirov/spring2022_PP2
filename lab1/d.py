x = int(input())
z = str(input())


if z=="k":
    c = int(input())
    d = x/1024
    d = round(d,c)
    print(d)
    exit()
else:
     d = x*1024
     print(d)
     exit()
