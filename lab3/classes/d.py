import math

class Point:
    x = 0
    y = 0
    def init(self):
        pass
    def show(self):
        print(str(self.x), ',', str(self.y))
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
    def dist(self, distx, disty):
        distance = math.sqrt(pow(distx - self.x,2) + pow(disty - self.y,2))
        print("Distance between two points: ", str(distance))

p1 = Point()
newp = input('Enter new pos: ').split(',')
p1.move(int(newp[0]), int(newp[1]))
p1.show()
p2 = input('Enter second point: ').split(',')
p1.dist(int(p2[0]), int(p2[1]))