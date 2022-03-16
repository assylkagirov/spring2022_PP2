class Shape():
    def __init__(self):
        pass
    def squarearea(self):
        return 0
    
class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length
    def squarearea(self):
        return self.length*self.length
    
num = Square(int(input()))
print(num.squarearea())
