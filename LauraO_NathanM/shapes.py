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


class Square: 
      def __init__(self):
        self.__side = ''

        @property 
        def side(self):
            return self.__side 

      

    


class Rectnage: 
    pass
 