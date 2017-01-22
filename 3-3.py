# -*- coding: UTF-8 -*-

# 如何使用生成器函数实现可迭代对象,即实现了__iter__方法


class PrimNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrime(self, k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start, self.end):
            if self.isPrime(k):
                yield k


for x in PrimNumbers(1, 100):
    print(x)
