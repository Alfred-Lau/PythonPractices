# -*- coding: UTF-8 -*-

# 如何创建可管理的对象属性

from math import pi


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        if not isinstance(radius, (int, float)):
            raise ValueError('wrong type')
        self.radius = float(radius)

    def getArea(self):
        return self.radius ** 2 * pi

    R = property(getRadius, setRadius)

c = Circle(3.2)
print(c.R)
c.R = 5.9
print(c.R)
print(c.getArea())

