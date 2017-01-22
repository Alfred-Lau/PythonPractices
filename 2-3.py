# -*- coding: UTF-8 -*-
# 如何统计序列中元素的出现频度


"""
方法一:

"""

# from random import randint
#
# # 初始化一个列表
# data = [randint(0, 20) for _ in range(0, 30)]
#
# # 以列表中的元素作为key,0为值建立字典
# count = dict.fromkeys(data, 0)
#
# for x in data:
#     count[x] += 1

# print(count)


"""
方法二

"""
#
# from collections import Counter
#
# count2 = Counter(data)
# print(count2.most_common(3))

"""
英语文章词频统计
"""

import re
from collections import Counter

# 打开文件读,注意要标示模式和编码
fd = open('test.txt', 'r', encoding='utf-8')
text = fd.read()
# 正则表达式以非字符作为分隔;Counter需要传一个列表进去
count3 = Counter(re.split('\W+', text))
print(count3)
print(count3.most_common(3))





