x = str(input())
k=0

for ch in x: 
    d = ord(ch)
    k+=d
    
if k>300:
    print("It is tasty!")
else:
    print("Oh, no!")