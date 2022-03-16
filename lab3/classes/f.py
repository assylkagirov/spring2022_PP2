num=list(input().split(' '))
prime=list(filter(lambda x: all( int(x)% int(y) !=0 for y in range (2,int(x))) ,num ))
for i in range(len(prime)):
    print(prime[i], end = ' ')