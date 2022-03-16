n = int(input())

arr =[]

arr = list(map(int, input().split()[:n]))

arr.sort()

pr = arr[-1] * arr[-2]

print(pr)   