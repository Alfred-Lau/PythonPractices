# -*- coding: UTF-8 -*-

# 如何在环状数据结构(循环引用)中管理内存

"""
一般方法


import sys


class A(object):
    def __del__(self):
        print('in A.__del__')

a = A()
print(sys.getrefcount(a) - 1)

"""

# 其他解决方案


import weakref


class Data(object):
    def __init__(self, value, owner):
        self.owner = weakref.ref(owner)
        self.value = value

    def __str__(self):
        return "%s's data, value is %s" % (self.owner(), self.value)

    def __del__(self):
        print('in Date.__del__')


class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)

    def __del__(self):
        print('in Node.__del__')

node = Node(100)
del node
input('waiting...')




