# -*- coding: UTF-8 -*-

# 如何处理二进制文件

fd = open('1.mp4', 'rb')
print(fd.read(44))


import struct

# python3.x中二进制数据前面需要加小写b,什么都不加默认是Unicode字符串
# 小端序,默认
res = struct.unpack('h', b'\x01\x02')
# 大端序
res2 = struct.unpack('>h', b'\x01\x02')

print(res, res2)

