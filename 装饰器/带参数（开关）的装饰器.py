from functools import wraps
# 带参数的装饰器：（相当于开关）为了给装饰器传参
# F=True#为True时就把装饰器给加上了
F = False  # 为False时就把装饰器给去掉了


def outer(flag):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if flag:
                print('before')
                ret = func(*args, **kwargs)
                print('after')
            else:
                ret = func(*args, **kwargs)
            return ret

        return wrapper

    return dec


@outer(F)  # @wrapper
def hahaha():
    print('hahaha')


@outer(True)
def shuangwaiwai():
    print('shuangwaiwai')


hahaha()
shuangwaiwai()
