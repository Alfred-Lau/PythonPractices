# -*- coding: UTF-8 -*-

# 如何根据字典中值的大小, 对字典中的项排序

"""
1.使用内置函数sorted
2.

"""

# 方案一
from random import randint

# 字典解析创建随机成绩表
d = {x: randint(60, 100) for x in 'xyzabc'}

# 注意直接使用sorted对字典进行排序,就是对键排序

"""

As you are in python3 , use dict.items() instead of dict.iteritems()

iteritems() was removed in python3, so you can't use this method anymore.

Take a look at Python Wiki (Link)

In Built-in Changes part, it is stated that

Removed dict.iteritems(), dict.iterkeys(), and dict.itervalues().

Instead: use dict.items(), dict.keys(), and dict.values() respectively.

"""
s_d = sorted(zip(d.values(), d.keys()))
print(sorted(d.items(), key=lambda x: x[1]))

