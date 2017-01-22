# -*- coding: UTF-8 -*-

# 如何在一个for语句中迭代多个可迭代对象

from random import randint

chinese = [randint(60, 100) for _ in range(40)]
english = [randint(60, 100) for _ in range(40)]
math = [randint(60, 100) for _ in range(40)]

# 方案一:采用索引,缺点是有些结构不支持索引访问
for i in range(len(chinese)):
    print(chinese[i] + english[i] + math[i])


# 方案二:通用方法
# 并行(zip)
total = []
for c, e, m in zip(chinese, english, math):
    total.append(c + e + m)

print(total)

# 串行(chain)
from itertools import chain

e1 = [randint(60, 100) for _ in range(40)]
e2 = [randint(60, 100) for _ in range(42)]
e3 = [randint(60, 100) for _ in range(42)]
e4 = [randint(60, 100) for _ in range(39)]

count = 0
for x in chain(e1, e2, e3, e4):
    if x > 90:
        count += 1

print(count)
