# -*- coding: UTF-8 -*-

# 如何拆分含有多种分隔符的字符串

# python 2.x 的解决办法
# def mySplit(text, ds):
#     res = [text]
#     for d in ds:
#         t = []
#         map(lambda x: t.extend(x.split(d)), res)
#         res = t
#         print('ds')
#     return [x for x in res if x]
#
#
# s = 'ab;cd|efg|hi,kl|mn\topq;rst,uvw\txyz'
# print(mySplit(s, ';,|\t'))
#
#


# python3.x的实现方法

import re

s = 'ab;cd|efg|hi,kl|mn\topq;rst,uvw\txyz'
res = re.split(r'[;,|\t]+', s)
print(res)

