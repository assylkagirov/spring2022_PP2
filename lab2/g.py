number_of_demon = int(input())
a = {}
for i in range(number_of_demon):
    demon, weakness = input().split()
    if weakness in a:
        a[weakness] += 1
    else:
        a[weakness] = 1
number_of_slayer = int(input())
b = {}
for i in range(number_of_slayer):
    slayer, ability, demonkill = input().split()
    demonkill = int(demonkill)
    if ability in b:
        b[ability] += demonkill
    else:
        b[ability] = demonkill
demonleft = 0
for i in a:
    if i in b:
        if a[i] > b[i]:
            demonleft += a[i] - b[i]
    else:
        demonleft += a[i]
print("Demons left:", demonleft)