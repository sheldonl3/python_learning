class Target(object):  # 用户使用的接口
    def request(self):
        print("普通请求")


class Adaptee(object):  # 开发设计的接口
    def specific_request(self):
        print("特殊请求")


class Adapter(Target):  # 适配器类，使用用户的接口调用开发的接口
    def __init__(self):
        self.adaptee = Adaptee()

    def request(self):
        self.adaptee.specific_request()


if __name__ == "__main__":
    target = Adapter()
    target.request()
