import math
def volumesphere(radius):
    volume = (4/3)*(math.pi)*radius**3
    return volume

radius=int(input())
print(volumesphere(radius))