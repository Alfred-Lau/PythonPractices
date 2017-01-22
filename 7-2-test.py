# -*- coding: UTF-8 -*-

from demo72 import Player, Player2

p1 = Player('0001', 'JIM')
p2 = Player2('0001', 'JIM')

# 差集判断出两种方式相差的部分
# {'status', '__dict__', '__weakref__'}

print(set(dir(p1)) - set(dir(p2)))

import sys


print(sys.getsizeof(p1.__dict__))
