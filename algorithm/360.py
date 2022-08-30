'''
现在的调查问卷越来越多了，所以出现了很多人恶意刷问卷的情况，已知某问卷需要填写名字，
如果名字仅由大小写英文字母组成且长度不超过10，则我们认为这个名字是真实有效的，否则就判定为恶意填写问卷。
请你判断出由多少有效问卷（只要名字是真实有效的，就认为问卷有效）。
'''


def wenjian(lis):
    res = 0
    for each in lis:
        l = len(each)
        if l > 10:
            continue
        if each.isalpha():
            res += 1
    print(res)
    return


'''
给定一个1到N的排列P1到PN（N为偶数），初始时Pi=i（1≤i≤N），现在要对排列进行M次操作，每次操作为以下两种中一种：
①将排列的第1个数移到末尾；
②交换排列的第1个数与第2个数、第3个数与第4个数、...、第N-1个数与第N个数。
求经过这M次操作后得到的排列。

超时，草泥马的
'''


class pailei():
    def __init__(self, lis1, lis2):
        self.lis_ji = lis1
        self.lis_ou = lis2
        self.flag = 0

    def do_one(self):
        if self.flag == 0:
            num0 = self.lis_ji.pop(0)
            self.lis_ji.append(num0)
        else:
            num0 = self.lis_ou.pop(0)
            self.lis_ou.append(num0)
        self.do_two()

    def do_two(self):
        # i = 0
        # new = [0 for _ in range(len(self.lis))]
        # while (i < len(self.lis)):
        #     self.lis[i], self.lis[i + 1] = self.lis[i + 1], self.lis[i]
        #     i += 2
        # self.lis = new
        if self.flag == 1:
            self.flag = 0
        else:
            self.flag = 1

    def prin(self):
        if self.flag == 0:
            for i in range(len(self.lis_ou)):
                print(self.lis_ji[i], end=' ')
                print(self.lis_ou[i], end=' ')
        else:
            for i in range(len(self.lis_ou)):
                print(self.lis_ou[i], end=' ')
                print(self.lis_ji[i], end=' ')


def mai():
    lie1 = input().split()
    lie2 = input().split()
    lis1 = [i for i in range(1, int(lie1[0]) + 1, 2)]
    lis2 = [i for i in range(2, int(lie1[0]) + 1, 2)]
    # print(lis1, lis2)
    p = pailei(lis1, lis2)

    for i in lie2:
        if i == '1':
            p.do_one()
        elif i == '2':
            p.do_two()
    p.prin()


'''
在一张透明的纸上，用笔写下一个字符串。然后将纸翻面，请你判断正面和背面看到的字符串是否一样。 
请注意，字符串在正反面看上去一样，必须要求每个字符是左右对称的，比如'W'字符是左右对称的，而'N'不是。
'''


def fanzhuan(str):
    str2 = str[::-1]
    if str != str2:
        print("NO")
        return
    zimu = ['A', 'H', 'W', 'X', 'V', 'T', 'Y', 'U', 'M', 'I', 'O']
    for i in range(len(str)):
        if str[i] != str2[i]:
            print('NO')
            return
        if str[i] not in zimu:
            print('NO')
            return
    print('YES')


def do_fanzhuan():
    while True:
        try:
            lie1 = input()
            fanzhuan(lie1)
        except:
            break


'''
魔塔是一款时尚经典小游戏，我们将魔塔简化后的规则描述如下：

魔塔有n关，而你可以自由选择前往攻略哪一关，每一关只能获得一次分数。第i关攻略完成后，你将会获得ai的分数。
某些关有一个特殊的宝物，你只能在攻略完这一关的时候使用这个宝物（也可以不使用，额外的宝物并不能留到其他关卡使用），
这个宝物将使得这一关不得分，但是将你现有的总得分乘以2作为新的得分。

你现在知道了所有关卡的通关方法，也知道了每一关的得分和是否有宝物，你现在想知道，怎么选择攻略的顺序和使用宝物的方法才能让自己的得分最大化？
'''


def momtai(data_nohave, data_have):
    res = 0
    for i in range(len(data_nohave)):
        res += data_nohave[i]

    data_have.sort()
    # print(data_have)
    for i in range(len(data_have) - 1, -1, -1):
        if data_have[i] > res:
            res += data_have[i]
        else:
            res *= 2
    print(res)


def do_motai():
    num = int(input())
    data_nohave = []
    data_have = []
    for i in range(num):
        da = input().split()
        if da[1] == '0':
            data_nohave.append(int(da[0]))
        else:
            data_have.append(int(da[0]))
    momtai(data_nohave, data_have)


if __name__ == '__main__':
    do_motai()
