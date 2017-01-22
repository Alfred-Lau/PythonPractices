# -*- coding: UTF-8 -*-

# 如何为创建大量实例节省内存


class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level


class Player2(object):
    # 不允许动态属性绑定,故能够节省内存
    __slots__ = ['uid', 'name', 'stat', 'level']

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

