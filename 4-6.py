# -*- coding: UTF-8 -*-

# 如何去掉字符串中不需要的字符

"""
方法一:str.strip()
"""
s1 = '   abc   123   '

# 对中间的空白无能为力
print(s1.strip())

s2 = '---abc+++'

print(s2.strip('-+'))


"""

方法二:

"""
s3 = 'abc:123'

res = s3[:3] + s3[4:]
print(res)

"""
方法三: str.replace, re.sub

"""

"""
方法四: str.translate, unicode.translate
"""




