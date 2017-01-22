# -*- coding: UTF-8 -*-

# 如何让类支持比较操作


# class Rectangle(object):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def area(self):
#         return self.w * self.h
#
#     def __lt__(self, other):
#         return self.area() < other.area()
#
#     def __le__(self, other):
#         return self.area() <= other.area()
#
# r1 = Rectangle(5, 3)
# r2 = Rectangle(4, 4)
#
# # 相当于调用r1.__lt__(r2)
# print(r1 < r2)


"""
使用functiontool简化
"""

from functools import total_ordering


@total_ordering
class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

r1 = Rectangle(5, 3)
r2 = Rectangle(4, 4)

# 相当于调用r1.__lt__(r2), 所以需要注意顺序
print(r1 < r2)


"""
定义抽象基类,简化比较
"""


from functools import total_ordering
from abc import ABCMeta, abstractclassmethod
from math import pi

@total_ordering
class Shape(object):
    @abstractclassmethod
    def area(self):
        pass

    def __lt__(self, other):
        print('in __lt__')
        if not isinstance(other, Shape):
            raise TypeError('not a shape')
        return self.area() < other.area()

    def __eq__(self, other):
        print('in __eq__')
        if not isinstance(other, Shape):
            raise TypeError('not a shape')
        return self.area == other.area()


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * pi

r1 = Rectangle(5, 3)
r2 = Rectangle(4, 4)
c1 = Circle(4)

print(c1 <= r1)
print(r1 > c1)
