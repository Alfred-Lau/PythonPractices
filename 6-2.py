# -*- coding: UTF-8 -*-

# 如何读写json数据

import json

l = [1, 2, 3, 4, 5, 'abc', {'name': 'bob', 'age': 13}]


# none--->null
print(json.dumps(l))
print(json.dumps(l, separators=[',', ':'], sort_keys=True))

l2 = json.loads('[1, 2, 3, 4, 5, "abc", {"age": 13, "name": "bob"}]')
print(l2)

# 区别:dump和dumps,前者的参数是一个文件
with open('6-2.json','w') as wf:
    json.dump(l, wf)
