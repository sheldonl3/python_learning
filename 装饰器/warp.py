from functools import wraps


class Log():
    def __init__(self, path='/home/sheldon13/Desktop/log'):
        self.log_path = path

    def __call__(self, func):
        @wraps(func)  # 防止重写函数名字和注释文档
        def warp_func(*args, **kwargs):
            log_nofity = func.__name__ + ' is calling'
            print(log_nofity)
            with open(self.log_path, 'a') as log_file:
                log_file.write(log_nofity + '\n')
            self.nofity()
            return func(*args, **kwargs)

        return warp_func

    def nofity(self):
        pass


class log_email(Log):  # 装饰器继承，重写包装函数里面的方法
    def __init__(self, email='xxxx', *args, **kwargs):
        super(log_email, self).__init__(*args, **kwargs)
        self.email = email

    def nofity(self):
        print(self.email)


if __name__ == '__main__':
    @Log('/home/sheldon13/Desktop/log5')
    def add(a, b):  # add=log_email(add)->__call__(add)->package
        print(a + b)
        return


    add(1, 6)
