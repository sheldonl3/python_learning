'''定义一个创建对象的接口，让其子类自己决定实例化哪一个工厂类，工厂模式使其创建过程延迟到子类进行。
根据用户输入的不同，调用相同的工厂，将会输出不同的结果。'''
class Person:
    def __init__(self, name,gender):
        self.name = name
        self.gender = gender

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender


class Male(Person):
    def __init__(self, name):
        super().__init__(name,'male')
        print('Got Mr.' + name)


class Female(Person):
    def __init__(self, name):
        super().__init__(name,'female')
        print('Got Miss.' + name)


class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Female(name)


if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("Chetan", "M")
    print(person.getName(),person.getGender())
