'''
多个装饰器装饰一个函数，前面装饰器调用的函数是后面装饰器装饰过的
'''
from functools import wraps


def dec1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('in dec1: before')
        ret = func(*args, **kwargs)  # 运行第二个装饰器装饰之后的func
        print('in dec1: after')
        return ret

    return wrapper


def dec2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('in dec2: before')
        ret = func(*args, **kwargs)
        print('in dec2: after')
        return ret

    return wrapper


@dec1
@dec2
def work():  # work=dec1(dec2(work))
    print('饿了吗')
    return 0


print(work())
