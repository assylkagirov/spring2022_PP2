from tabnanny import check

n = int(input())

def check_divisible(num):
    if num % 3 == 0 and num % 4 == 0:
        return True

for i in range(n):
    if i < n:
        if check_divisible(i):
            print(str(i), end = " ")