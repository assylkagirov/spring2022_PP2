x, z  = map(int, input().split())

def isprime(x):
    for i in range(2, int(x**1/2)+1):
        if x%i == 0:
            return False
    return True        

if x<500 and z%2==0 and isprime(x):
    print("Good job!")
else:
    print("Try next time!")