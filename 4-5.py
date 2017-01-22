# -*- coding: UTF-8 -*-

# 如何对字符串进行左, 右, 居中对齐

example = {
    'DistCull': 500.0,
    'SmallCull': 0.04,
    'farclip': 477,
    'lodDist': 100.0,
    'triliner': 40
}

# 取得最大长度
width = max(map(len, example.keys()))

for x in example:
    # print(x.ljust(width), ':', example[x])
    print(format(x, '>' + str(width)), ':', example[x])

