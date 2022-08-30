'''
方法1:yield（生成器）可以很容易的实现上述的功能，从一个函数切换到另外一个函数
'''
import time


def task_1():
    while True:
        print("--This is task 1!--before")
        yield
        print("--This is task 1!--after")
        time.sleep(0.5)


def task_2():
    while True:
        print("--This is task 2!--before")
        yield
        print("--This is task 2!--after")
        time.sleep(0.5)


'''
生成器的send用法 generator.send(value)
'''


def test_for_send():
    def test():
        i = 1
        while i < 5:
            temp = yield i ** 2
            print(temp)
            i += 1

        t = test()
        # 第一次运行只能使用next或者send(None)
        print(t.__next__())
        print('sss')
        # send的作用相当于使生成器继续运行，并且传递的参数为yield的返回值(程序中即temp的值)
        print(t.send("Hello World"))
        print('sss2')
        print(t.__next__())  # 相当于send(None) 此时temp = None


'''
greenlet已经实现了协程，但是这个需要人工切换，很麻烦
'''
from greenlet import greenlet

def task_1():
    while True:
        print("--This is task 1!--")
        g2.switch()  # 切换到g2中运行
        time.sleep(0.5)


def task_2():
    while True:
        print("--This is task 2!--")
        g1.switch()  # 切换到g1中运行
        time.sleep(0.5)


'''
python中还有一个比greenlet更强大的并且能够自动切换任务的模块gevent，
其原理是当一个greenlet遇到IO(比如网络、文件操作等)操作时，比如访问网络，
就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。
由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，
就保证总有greenlet在运行，而不是等待IO
'''
import gevent


def task(num):
    for i in range(num):
        print(gevent.getcurrent(), i)
        gevent.sleep(1)  # 模拟一个耗时操作，注意不能使用time模块的sleep


if __name__ == "__main__":
    # t1 = task_1()  # 生成器对象
    # t2 = task_2()
    # # print(t1, t2)
    # while True:
    #     next(t1)  # 1、唤醒生成器t1，执行到yield后，保存上下文，挂起任务；下次再次唤醒之后，从yield继续往下执行
    #     print("The main thread!")  # 2、继续往下执行
    #     next(t2)  # 3、唤醒生成器t2，....
    #     print()

    # g1 = greenlet(task_1)  # 定义greenlet对象
    # g2 = greenlet(task_2)
    # g1.switch()  # 切换到g1中运行

    g1 = gevent.spawn(task, 5)  # 创建协程
    g2 = gevent.spawn(task, 5)
    g3 = gevent.spawn(task, 5)

    g1.join()  # 等待协程运行完毕
    g2.join()
    g3.join()
