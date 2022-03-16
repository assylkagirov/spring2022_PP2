import math

x, y = map(int, input().split())
number_points = int(input())
temp = []
dists = []
for i in range(number_points):
    key = input()
    temp.append(key.split())
for i in temp:
    n = math.sqrt(pow(int(i[0]) - x, 2) + pow(int(i[1]) - y, 2))
    dists.append(n)
dists.sort()
for i in dists:
    for j in temp:
        if i == math.sqrt(pow(int(j[0]) - x, 2) + pow(int(j[1]) - y, 2)):
            print(j[0], j[1])
            temp.remove(j)