'''
第一题
A+B问题又来了。
设a，b，c是0到9之间的整数（其中a，b，c互不相同），其中abc和acc是两个不同的三位数，现给定一正整数n，问有多少对abc和acc能满足abc+acc=n（a≠0）？
一个正整数n（100<n<2000）。
'''


def abc(input):
    res = 0
    reslist = []
    for a in range(1, 10):
        for c in range(10):
            if a == c:
                continue
            acc = a * 100 + c * 10 + c
            abc = input - acc
            if abc <= 100 or abc > 1000:
                continue
            nb = int(str(abc)[1])
            na = int(str(abc)[0])
            nc = int(str(abc)[2])

            if na == a and nc == c and nb != a and nb != c:
                res += 1
                reslist.append([abc, acc])
    print(res)
    l = len(reslist)
    for i in range(l):
        print(reslist[l - i - 1][0], reslist[l - i - 1][1])


# 第一题:斐波那契蛇
def feibonaq(n):
    nf = n * n
    n1 = 0
    n2 = 1
    count = 2

    if n <= 0:
        return
    elif n == 1:
        print('1')
        return
    else:
        lis = [1, 1]
        while count < nf:
            new = n1 + n2
            lis.append(new)
            n1 = n2
            n2 = new
            count += 1
        lis.append(n1 + n2)
        lis.reverse()
        num = 0

        res = [[0] * (n) for i in range(n)]

        print(lis)
        for i in range(n):
            for j in range(i, n - i):
                res[i][j] = lis[num]
                num += 1
            for j in range(1 + i, n - i):
                res[j][n - 1 - i] = lis[num]
                num += 1
            for j in range(n - i - 2, i - 1, -1):
                res[n - i - 1][j] = lis[num]
                num += 1
            for j in range(n - 2 - i, i, -1):
                res[j][i] = lis[num]
                num += 1

        for each in res:
            for i in each:
                print(i, end=' ')
            print()


if __name__ == '__main__':
    a = input()
    # abc(int(a))
    feibonaq(int(a))
