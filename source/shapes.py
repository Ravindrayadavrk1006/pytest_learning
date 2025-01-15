import math
class Shape:
    def area(self):
        pass
    def parameter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi* self.radius**2
    
    def parameter(self):
        return 2*math.pi* self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length* self.width
    
    def parameter(self):
        return 2*(self.length + self.width)
    
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return other.length == self.length and other.width == other.width
        
class Square(Rectangle):
    def __init__(self, side):
        #pass the length and breadth as side 
        super().__init__(side, side)
