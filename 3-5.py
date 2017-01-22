# -*- coding: UTF-8 -*-

# 如何对迭代器做切片操作

"""
解决方案一:
lines = open('test.txt').readlines()
lines[200:300]

缺点:
1.文件过大的时候,readlines函数一次性读进内存,性能问题.
2.当使用过readlines之后,需要fseek(0)函数吧文件指针移到头部
"""

from itertools import islice

