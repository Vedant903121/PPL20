import turtle

s = turtle.getscreen()
t = turtle.Turtle()

class shape:
    def __init__(self, sides = 0, length = 0):
        self.sides = sides
        self.length = length

class polygon(shape):
    def info(self):
        print('In geometry a polygon can be defined as a flat or plane, two dimensional with straight sides')

class square(polygon):
    def show(self):
        for i in range(4):
            t.fd(self.length)
            t.rt(90)

class pentagon(polygon):
    def show(self):
        for i in range(5):
            t.fd(self.length)
            t.left(72)

class hexagon(polygon):
    def show(self):
        for i in range(6):
            t.fd(self.length)
            t.left(60)

class octagon(polygon):
    def show(self):
        for i in range(8):
            t.fd(self.length)
            t.left(360/8)
class heptagon(polygon):
    def show(self):
        for i in range(7):
            t.fd(self.length)
            t.left(360/7)
a = heptagon()
a.length = 45
a.show()
        
        
