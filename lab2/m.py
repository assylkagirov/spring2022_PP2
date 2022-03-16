k = 0
dates = [[99999] * 3 for l in range(100000)]
for i in range(100000):
    try:
        dates[i][0], dates[i][1], dates[i][2] = input().split(' ')
        k += 1
    except:
        break
datessorted = [1000000] * k
for i in range(k):
    datessorted[i] = int((dates[i][2]) + (dates[i][1]).rjust(2,"0") + (dates[i][0]).rjust(2,"0"))
datessorted.sort()
for i in range(k):
    datessorted[i] = str(datessorted[i]).rjust(8, "0")
    temparr = list(datessorted[i])
    print(str(temparr[6] + temparr[7]), str(temparr[4] + temparr[5]), str(temparr[0] + temparr[1] + temparr[2] + temparr[3]))