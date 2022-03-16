N = int(input())
password = ["zzzzzzzzzzz"] * 1000
safepasswords = ["zzzzzzzzzzz"] * 1000
isUpper = False
isLower = False
isNumber = False
k = 0
templer = ""
for i in range(N):
    password[i] = input()
    if any(char.isupper() for char in password[i]) and isUpper != True:
        isUpper = True
    if any(char.islower() for char in password[i]) and isLower != True:
        isLower = True
    if any(char.isdigit() for char in password[i]) and isNumber != True:
        isNumber = True
    for o in range(k):
        if safepasswords[o] == password[i]:
            isNumber = False
    if isUpper and isLower and isNumber:
        safepasswords[k] = password[i]
        k = k + 1
    isUpper = False
    isLower = False
    isNumber = False
print(str(k))
safepasswords.sort()
for i in range(k):
    print(safepasswords[i])