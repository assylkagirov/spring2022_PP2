import math 

numside = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))

apothem = length/(2 * math.tan(math.pi/numside))
area = int(numside*length*apothem/2)

print("The area of the polygon is: ", area)