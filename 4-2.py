# -*- coding: UTF-8 -*-

# 如何判断字符串a是否以字符串b开头或结尾

import os, stat

res = [item for item in os.listdir('.') if item.endswith(('sh', 'py'))]

for x in res:
    # 修改执行权限为可执行
    os.chmod(x, os.stat(x).st_mode | stat.S_IXUSR)
