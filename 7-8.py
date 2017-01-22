# -*- coding: UTF-8 -*-


# 如何通过实例方法名字的字符串调用方法

from math import pi


class Circle(object):
    def __init__(self, r):
        self.r = r

    def Area(self):
        return self.r ** 2 * pi


class Triangle(object):
    def __init__(self, h1, h2, h3):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3

    def get_area(self):
        return self.h1 * self.h2 / 2


class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height


def getArea(shape):
    for name in ('Area', 'getArea', 'get_area'):
        f = getattr(shape, name, None)
        if f:
            return f()

shape1 = Circle(2)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(6, 4)
shapes = [shape1, shape2, shape3]

"""

上面print时，加了list转换，是为了python2/3的兼容性.在python2中map直接返回列表，但在python3中返回迭代器.因此为了兼容python3, 需要list转换一下

"""

print(list(map(getArea, shapes)))


"""
使用 methodcaller

from operator import methodcaller

s = 'abc123abc456'
print(methodcaller('find', 'abc', 4)(s))

"""