# f(n)=1/5-1/10+1/15-1/20+1/25-......+1/(5*(2*n-1))-1/(5*2*n)。
import math


def masd():
    a = input()
    a = int(a)
    if a == 0:
        return 0
    res = 0
    for i in range(a):
        res += 1 / (5 * (2 * (i + 1) - 1))
    for i in range(a):
        res -= 1 / (5 * (2 * (i + 1)))

    print(format(res, '.4f'))


def prime(m):
    count = 0
    for i in range(2, int(math.sqrt(m)) + 1):
        if m % i == 0:
            count = 1
        if count != 1:
            return True
        else:
            return False


def palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


def li():
    res = 0
    a = input().split()
    n1, n2 = int(a[0]), int(a[1])
    # for num in range(n1,n2+1):
    num = n1
    while num <= n2:
        tmp = str(num)
        l = len(tmp)
        if l == 2:
            res += 1
            continue
        for i in range(l):
            tmpnum = tmp[:i] + tmp[i + 1:]
            while tmpnum[0] == '0':
                tmpnum = tmp[:0] + tmp[1:]
            tmpnum = int(tmpnum)
            # print(tmpnum)
            if prime(tmpnum) and palindrome(tmpnum):
                res += 1
                num += 1
                if i == l - 1:
                    num += 10
                    res += 9
                break
        num += 1

    print('res=', res)


if __name__ == '__main__':
    li()
