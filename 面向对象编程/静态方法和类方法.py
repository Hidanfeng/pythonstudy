from math import sqrt

class Triangle(object):
    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a,b,c):
        return a +b >c



obj = Triangle(3,4,5)
obja = obj.is_valid(3,4,5)
a = Triangle.is_valid(3,4,5)
print(a)
print(obja)