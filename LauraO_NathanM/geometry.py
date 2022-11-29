class Point (object):
    def __init__ (self, x,y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

class Line (object):
    def __init__ (self, from_point,to_point):
        self.__from_point= from_point
        self.__to_point= to_point

    @property
    def from_point(self):
        return self.__from_point

    @property
    def to_point(self):
        return self.__to_point

    @from_point.setter
    def from_point(self, from_point):
        self.__from_point = from_point

    @to_point.setter
    def to_point(self, to_point):
        self.__to_point = to_point

    @property
    def length(self):
        return ((self.__to_point.x-self.__from_point.x)**2+
            (self.__to_point.y-self.__from_point.y)**2)**0.5



class Polyline (object):
    def __init__ (self):
        self.__segments = []

    @property
    def length(self):
        total = 0
        for line in self.__segments:
            total += line.length
        return total

    def add_segment(self, seg):
        return self.__segments.append(seg)

    @property
    def segments(self):
        return self.__segments
