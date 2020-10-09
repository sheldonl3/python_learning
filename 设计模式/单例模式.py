'''
单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。
当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。

比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。
如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建 AppConfig 对象的实例，
这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。事实上，
类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象
'''
import threading


class Singleton(object):
    _instance_lock = threading.Lock()  # 多线程加锁;在加锁前后都进行单例判断

    def __init__(self, path):
        self.path = path

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):#双重校验锁
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


if __name__ == '__main__':
    obj1 = Singleton('sdd')  # 构造的时候赋值没有效果
    obj1.path = 'obj1'
    obj2 = Singleton('')
    obj2.path = 'obj2'  # 只能通过实例来赋值，赋值的实例总是单例实例，对全部obj都有效
    print(obj1.path, obj2.path)


    def task():
        obj = Singleton('hhh')
        print(obj)


    for i in range(10):
        t = threading.Thread(target=task)
        t.start()
