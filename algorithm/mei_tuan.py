'''A国和B国正在打仗，他们的目的是n块土地。现在，A国和B国暂时休战，为了能合理分配这一些土地，AB国开始协商。
A国希望得到这n块土地中的p块土地，B国希望得到这n块土地中的q块土地。每个国家都将自己希望得到的土地编号告诉了小团和小美——两位战争调和人。
你需要帮小团和小美计算，有多少块土地是只有A国想要的，有多少块土地是只有B国想要的，有多少块土地是两个国家都想要的。'''


def judge(a, tudi1, tudi2):
    res1, res2, gonggong = int(a[1]), int(a[2]), 0
    tudi = [0] * int(a[0])
    for i in tudi1:
        tudi[int(i) - 1] += 1
    for i in tudi2:
        if tudi[int(i) - 1] != 0:
            gonggong += 1
    res1 -= gonggong
    res2 -= gonggong
    print(res1, res2, gonggong)


'''在小美的国家，任何一篇由英文字母组成的文章中，如果大小写字母的数量不相同会被认为文章不优雅。
现在，小美写了一篇文章，并且交给小团来修改。小美希望文章中的大小写字母数量相同，所以她想让小团帮她把某
些小写字母改成对应的大写字母，或者把某些大写字母改成对应的小写字母，使得文章变得优雅。
小美给出的文章一定是由偶数长度组成的，她想知道最少修改多少个字母，才能让文章优雅。'''


def daxiaoxie(str):
    da, xiao = 0, len(str)
    daxie = []
    for i in range(65, 91):
        daxie.append(chr(i))
    for each in str:
        if each in daxie:
            da += 1
    xiao -= da
    print(xiao, da)
    print((max(da, xiao) - min(xiao, da)) // 2)


'''在小团的公司中，有n位员工。除了最高领导——小团外，每位员工有且仅有一位直接领导。所以，公司内从属关系可以看成一棵树。
现在，公司接到一个项目，需要重新划分这n位员工的从属关系。新的划分描述如下：
1.每个人要么没有下属，要么有至少两个直接下属（即至少有两人的直接领导为这个人）
2.第 i 个人的下属（包括自己）有恰好 ai 个。
请注意，直接下属和下属（包括自己）可分别看做树上点的"儿子"和"子树"。
请问是否存在这么一种关系？注意，输入不会给出最高领导的编号'''


def xiashu(nums):
    i = 0
    while i < len(nums):
        num = nums[i][0]
        lis = nums[i + 1]
        if 2 in lis:
            print('NO')
            return

        lis.sort()
        lis = lis[::-1]
        print(lis)

        num1 = 0
        for i in range(len(lis)):
            if lis[i] == 1:
                num1 = num - i
                lis = lis[:i]
                break

        print(lis, num1)
        l = len(lis)
        for x in range(len(lis)):
            num1 -= lis[x] - 1 - (l - 1 - x)
        if num1 == 0:
            print('YES')
        else:
            print('NO')


'''
if __name__ == '__main__':
    res = []
    while True:
        try:
            s = input().split()
            for i in range(len(s)):
                s[i] = int(s[i])
            res.append(s)
        except:
            break
    xiashu(res)
'''
'''
小团所在的班级今天去郊游了。小团的班级有n个人，每个人有一个独一无二的正整数学号ai。因为小团的班级很大（n可能达到10^9这么大！），点名成为了一个重大的问题。
小团作为班长，他想让同学们站成一列，他点名的方式如下：
1.如果当前点到的同学不在队列中，则加入队列中的第一个
2.如果当前点到的同学在队列中，则该同学出队，站到队列中第一个，并且不保留他之前的空位。
现在，给出小团的点名顺序，请你算出队列中同学是怎么排的。注意，点名可能存在重复，也可能只点名一部分同学。
反向找
'''

'''
齿轮
'''
import copy
import sys


def chilun(num, str, res, start):
    print(str, res, start)
    if str in res:
        return
    else:
        res.append(copy.deepcopy(str))

    for i in range(start, num):
        if i == 0:
            if str[0] != 'Z' and str[1] != 'A':
                tmp = copy.deepcopy(str)
                tmp[0] = chr(ord(tmp[0]) + 1)
                tmp[1] = chr(ord(tmp[1]) - 1)
                chilun(num, tmp, res, i + 1)
        elif i == l - 1:
            if str[l - 1] != 'Z' and str[l - 2] != 'A':
                tmp = copy.deepcopy(str)
                tmp[l - 1] = chr(ord(tmp[l - 1]) + 1)
                tmp[l - 2] = chr(ord(tmp[l - 2]) - 1)
                chilun(num, tmp, res, i + 1)
        else:
            if str[i] != 'Z' and str[i - 1] != 'A':
                tmp = copy.deepcopy(str)
                tmp[i] = chr(ord(tmp[i]) + 1)
                tmp[i - 1] = chr(ord(tmp[i - 1]) - 1)
                chilun(num, str, res, i + 1)
            if str[i] != 'Z' and str[i + 1] != 'A':
                tmp = copy.deepcopy(str)
                tmp[i] = chr(ord(tmp[i]) + 1)
                tmp[i + 1] = chr(ord(tmp[i + 1]) - 1)
                chilun(num, tmp, res, i + 1)

    return len(res)


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    while True:
        try:
            num = int(input())
            str = input()
        except:
            break
        l = len(str)
        print(chilun(num, [x for x in str], [], 0))
