a = int(input())
b = int(input())

def squares(num):
    return pow(num, 2)

for i in range(a, b+1, 1):
    print(str(squares(i)))