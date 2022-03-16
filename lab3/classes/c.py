class Shape():
    def __init__(self):
        pass
    def rectanglearea(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width ):
        Shape.__init__(self)
        self.length = length
        self.width = width
        
    def rectanglearea(self):
        return self.length*self.width
    
x, z  = map(int, input().split())
    
num = Rectangle(x, z )
print(num.rectanglearea())
