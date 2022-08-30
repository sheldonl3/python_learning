def wrong_fib(num):
    fcb = [0, 1, 1]
    if num <= 2:
        return 1
    for i in range(3, num + 1):
        if i % 2 == 0:
            fcb.append(fcb[i - 1] + fcb[i - 3])
        else:
            fcb.append(fcb[i - 1] + fcb[i - 2])
    return fcb[-1]


from collections import defaultdict

'''
中心扩散法找回文子串
'''


def getSubLen(s):
    l = len(s)
    if l == 1:
        return l
    res = ''
    for i in range(l):
        tmp = spread(s, i, i)
        if len(tmp) > len(res):
            res = tmp
    for i in range(l):
        tmp = spread(s, i, i + 1)
        if len(tmp) > len(res):
            res = tmp
    return len(res)


def spread(s, left, right):
    dic = defaultdict(int)

    while left >= 0 and right <= len(s) - 1 and s[left] == s[right] and dic[s[left]] < 2 and dic[s[right]] < 2:
        dic[s[left]] += 1
        dic[s[right]] += 1
        left -= 1
        right += 1

    if right > left + 1:
        return s[left + 1:right]
    elif right == left + 1:
        return ''
    return s[left]


if __name__ == '__main__':
    a = input()
    print(getSubLen(a))
