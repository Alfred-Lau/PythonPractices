# -*- coding: UTF-8 -*-

# 如何定义带参数的装饰器


# 工厂函数,生产函数装饰器
from inspect import signature


def typeassert(*ty_args, **ty_kargs):
    def decorator(func):
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments

        def wrapper(*args, **kargs):
            for name, obj in sig.bind(*args, **kargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('%s must be %s' % (name, btypes[name]))
            return func(*args, **kargs)

        return wrapper

    return decorator


@typeassert(int, str, list)
def f(a, b, c):
    print(a, b, c)


f(1, 'abc', [])
f(1, 5, [])

