# -*- coding: UTF-8 -*-

# 如何派生内置不可变类型并修改实例化行为

class IntTuple(tuple):

    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)

t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
print(t)
