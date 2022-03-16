x = int(input())

arr =[]

for i in range(x):
    z=int(input())
    arr.append(z)
    
    
for i in range(x):
    if arr[i] <= 10:
        print("Go to work!")
    elif arr[i] > 10 and arr[i] <= 25:
        print("You are weak")
    elif arr[i] > 25 and arr[i] <= 45:
        print("Okay, fine")
    else:
        print("Burn! Burn! Burn Young!")
        
