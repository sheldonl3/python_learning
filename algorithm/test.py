'''python默认的递归深度是很有限的，大概是900多的样子，
当递归深度超过这个值的时候，就会引发这样的一个异常。
解决的方式是手工设置递归调用深度，方式为'''
import sys

sys.setrecursionlimit(1000000)


def sort_tuple(tupl):
    lis = list(tupl)
    lis.sort()
    return tuple(lis)


if __name__ == '__main__':
    # b = input().split()  # 输入字符数组正确
    # a = [int(i) for i in input().split()]  # 输入数字数组正确方式
    # print(b)
    # print(a)
    t = (1, 4, 5, 6, 2)
    print(sort_tuple(t))
    map={1:2,3:5,2:6}

    print(list(map))
