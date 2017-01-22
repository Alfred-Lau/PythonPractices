# -*- coding: UTF-8 -*-

# 如何调整字符串中文本的格式

import re

log = open('4-3.log', 'r', encoding='utf-8').read()

# 使用捕获组\n代表第n个组
"""

第二种重命名的写法:
res = re.sub('(?P<hour>\d{2}:(\d{2}):(\d{2})', r'\g<hour>-\2-\3', log)

"""
res = re.sub('(\d{2}):(\d{2}):(\d{2})', r'\1-\2-\3', log)
print(res)
