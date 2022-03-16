array = list(map(int, input().split()))
now = 0
bool = False
n = len(array) - 1

for i in range(len(array)):
    if i > now:
        bool = False
        break
    if array[i] + i > now:
        now = array[i]+i
    if now >= n:
        print(1)
        bool = True
        break
if bool == False:
    print(0)