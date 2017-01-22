# -*- coding: UTF-8 -*-

# 如何进行反向迭代以及如何实现反向迭代

# 对列表(即序列)[ ]进行反序的实现方法:

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
# 1.改变原列表
l1.reverse()
print(l1)

# 2.不改变原列表,但生成一个新的等大小列表
print(l2[::-1])

# 3.使用reversed()方法生成一个迭代器列表对象,该方法和iter()方法作用相反

for x in reversed(l2):
    print(x)


class FloatRange:
    def __init__(self, start, end, step = 0.1):
        self.start = start
        self.end = end
        self.step = step
    # 正向迭代器

    def __iter__(self):
        res = self.start
        while res <= self.end:
            yield res
            res += self.step
    # 反向迭代器

    def __reversed__(self):
        res = self.end
        while res >= self.start:
            yield res
            res -= self.step

# 测试
# 正向迭代器
for x in FloatRange(5, 50, 5):
    print(x)
# 反向迭代器
for x in reversed(FloatRange(5, 50, 5)):
    print(x)
