# -*- coding: UTF-8 -*-

# 如何使用描述符对实例属性做类型检查


class Descriptor(object):
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError('expected an %s' % self.type_)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Person(object):
    name = Descriptor('name', str)
    age = Descriptor('age', int)
    height = Descriptor('height', float)


p = Person()
p.name = 'Bob'
print(p.name)
p.age = '17'


