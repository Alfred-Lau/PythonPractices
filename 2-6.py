# -*- coding: UTF-8 -*-

# 如何让字典{}保持有序,即按照进入字典的顺序可以被访问

# from collections import OrderedDict
#
# d = OrderedDict()
# d['Jim'] = (1, 35)
# d['Leo'] = (2, 37)
# d['Bob'] = (3, 40)
# for x in d:
#     print(x)


from time import time
from random import randint
from collections import OrderedDict

d = OrderedDict()
players = list('ABCDEFGH')
start = time()

for i in range(8):
    # raw_input in python 2 was renamed to input in python 3
    input()
    p = players.pop(randint(0, 7-i))
    end = time()
    print(i + 1, end - start)
    # fmt: {'Leo': (ranking, time)}
    d[p] = (i + 1, end - start)

print()
print('*' * 20)

for k in d:
    print(k, d[k])
