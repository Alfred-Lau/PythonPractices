# -*- coding: UTF-8 -*-

# 如何快速找到多个字典中的公共键(key)

# # sample模块用来随机取样
# from random import randint, sample
#
# # 第一轮比赛
# s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
# # 第二轮比赛
# s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
# # 第三轮比赛
# s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
#
# res = []
# for k in s1:
#     if k in s2 and k in s3:
#         res.append(k)
#
# print(res)


"""
方案二:

"""

from random import randint, sample
from functools import reduce

# 第一轮比赛
s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
# 第二轮比赛
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
# 第三轮比赛
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
dict_res = reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3]))

print(dict_res)
