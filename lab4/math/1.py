import math 

def degreetoradian(degree):
    radian = (degree * math.pi)/180
    return radian

degree = int(input("Input degree: "))
print("Output radian: ",degreetoradian(degree))