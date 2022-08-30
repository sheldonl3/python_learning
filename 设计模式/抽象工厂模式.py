'''
根据用户输入的不同，调用相同的接口，去调用不同的工厂进行不同的生产，得出不同的输出结果。
例如：
在编写一款面向全年龄的游戏，游戏本身需要使用工厂方法进行开发。
但游戏也需要考虑不同年龄段玩家的需求和口味不同，所以需要为不同年龄段的玩家针对游戏进行一定的修改。
于是在用户输入年龄后，运行符合其年龄的要求的游戏。
'''


class Frog(object):
    '''青蛙类'''

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {} !'.format(self, obstacle, obstacle.action()))


class Bug(object):
    '''臭虫类'''

    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld(object):
    '''抽象工厂-青蛙世界'''

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '----------welcome to FrogWorld-------------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizerd(object):
    '''巫师类'''

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Wizerd battles against {} and {} !'.format(self, obstacle, obstacle.action()))


class Ork(object):
    '''怪兽类'''

    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizerdWorld(object):
    '''抽象工厂-巫师世界'''

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '--------welcome to WizerdWorld-------------------'

    def make_character(self):
        return Wizerd(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment(object):
    '''游戏主入口'''

    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validata_age(name):
    '''验证年龄'''
    try:
        age = input('welcome {}, How old are you?'.format(name))
        age = int(age)
    except Exception as e:
        print('Age {} is invalid,please try again...'.format(age))
        return (False, age)
    return (True, age)


def main():
    name = input("Hello,What's you name?")
    valid_input = False
    while not valid_input:
        valid_input, age = validata_age(name)
    game = FrogWorld if age < 18 else WizerdWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
    print('hello world')
