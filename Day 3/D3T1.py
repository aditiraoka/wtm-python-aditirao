from math import pi

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def getArea(self):
        return pi*self.radius**2

    def getCircumference(self):
        return 2*pi*self.radius


x = Circle(7)
print(round(x.getArea(),3))
