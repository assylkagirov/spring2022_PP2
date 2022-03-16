arrx = input("").split(' ')
if len(arrx) < 2:
    n = int(arrx[0])
    x = int(input())
else:
    x = int(arrx[1])
    n = int(arrx[0])
arr = [0] * n
xorval = 0
if x < 0 or x > 1000:
    print("Incorrect input for x")
elif n < 0 or n > 1000:
    print("Incorrect input for n")
else:
    for i in range(n):
        arr[i] = x + (2 * i)
    xorval = arr[0]
    for p in range(n):
        if p != 0:
            xorval = xorval ^ arr[p]
    print(xorval)