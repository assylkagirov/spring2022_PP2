arr1 = []
arrsize = 0
for i in range(99999999999999999999999999999999999999999999):
    arr1.append(int(input()))
    arrsize = arrsize + 1
    if arr1[i] == 0:
        del arr1[i]
        arrsize = arrsize - 1
        break
realsize = 0
if arrsize%2 == 0:
    realsize = int(arrsize/2)
else:
    realsize = int(((arrsize + 1) / 2))
arr2 = [0] * realsize
for i in range(realsize):
    arr2[i] = arr1[i] + arr1[(arrsize - 1) - i]
    if i == ((arrsize - 1) - i):
        arr2[i] = arr1[i]
for i in range(realsize):
    print(arr2[i], end = ' ')