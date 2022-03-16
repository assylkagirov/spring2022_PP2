N = int(input())
discs = ["XMLBEROQUARTODIMO"] * 400
discs1 = ["XMLBEROQUARTODIMO"] * 400
discsgiven = ["XMLBEROQUARTODIMO"] * 400
takendiscs = 0
k = 0
for i in range(N):
    try:
        discs[0], discs1[399 - k] = input().split(' ')
        k = k + 1
    except:
        discsgiven[takendiscs] = discs1[399 - takendiscs]
        del discs1[399 - takendiscs]
        takendiscs = takendiscs + 1
for l in range(takendiscs):
    print(discsgiven[l], end = ' ')        