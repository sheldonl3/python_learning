def remov_wuxiao_kuohao(s):
    def isinvaild(s):  # 判断有效
        num = 0
        for each in s:
            if each == '(':
                num += 1
            if each == ')':
                num -= 1
            if num < 0:
                return False
        return num == 0
    
    set1 = {s}
    while 1:
        res = list(filter(isinvaild, set1))
        if res:
            return res
        new_set = set()
        for each in set1:  # 广度遍历，删除（），每一种删除结果保存，进入下次循环；结果中有合法的就退出
            for i in range(len(each)):
                if each[i] in '()':
                    new_set.add(each[:i] + each[i + 1:])
        set1 = new_set


if __name__ == '__main__':
    s = ')('
    print(remov_wuxiao_kuohao(s))
