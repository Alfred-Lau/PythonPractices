# -*- coding: UTF-8 -*-

# 如何使用临时文件

from tempfile import TemporaryFile, NamedTemporaryFile

# python3.x 打开模式为w+
# 在 文件系统中找不到
f = TemporaryFile('w+')
f.write('as' * 100000)

f.seek(0)
print(f.read(20))

# 能在文件系统中找到
ntf = NamedTemporaryFile()
print(ntf.name)
