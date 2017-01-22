# -*- coding: UTF-8 -*-

# 如何读写文本文件

s = '你好'
print(s)
res = s.encode('utf-8')
print(res)

print(res.decode('utf-8'))

fd = open('5-1.txt', 'w', encoding='utf-8')
fd.write('你好')


fd2 = open('5-1.txt', 'r', encoding='utf-8')
print(fd2.read())


