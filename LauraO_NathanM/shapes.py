import math

class Circle: 
    def __init__(self):
        self.__radius = ''

    @property 
    def radius(self):
        return self.__radius 

    @radius.setter 
    def radius(self, radius):
        self.__radius = radius 

    @property 
    def area(self):
        return math.pi * (self.__radius ** 2)
    
    def __str__(self):
        return f'Circle area with a radius of {self.radius} is {self.area:.3f}'


class Square: 
    def __init__(self):
        self.__side = ''

    @property 
    def side(self):
        return self.__side 

    @side.setter
    def side(self, side):
        self.__side = side
        
    @property
    def area_sq(self):
        return (self.__side * self.__side)
    
    def __str__(self):
        return f'Square area with a side of {self.side} is {self.area_sq}'

class Rectangle: 
    def __init__(self):
        self.__length = ''
        self.__width = ''
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length):
        self.__length = length
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def area_rec(self):
        return (self.__length * self.__width)
    
    def __str__(self):
        return f'Rectangle area with a length of {self.length} and a width of {self.width} is {self.area_rec}'

 