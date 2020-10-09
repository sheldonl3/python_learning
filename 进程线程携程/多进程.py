from multiprocessing import Process, Queue
import os, time, random

'''
重写proccess类，start自动调用run方法
'''


class Run(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s runing' % self.name)
        time.sleep(random.randrange(1, 5))
        print('%s runing end' % self.name)


'''
multiprocessing模块就是跨平台版本的多进程模块。
multiprocessing模块提供了一个Process类来代表一个进程对象，
下面的例子演示了启动一个子进程并等待其结束
进程间通信:队列
'''


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # p1 = Run('anne')
    # p2 = Run('alex')
    # p3 = Run('ab')
    # p4 = Run('hey')
    # p1.start()  # start会自动调用run
    # p2.start()
    # p3.start()
    # p4.start()
    # p1.join()  # 等待p1进程停止
    # p2.join()
    # p3.join()
    # p4.join()
    # print('主线程')

    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
