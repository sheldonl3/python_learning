'''
给定一个正整数数n, 一个正整数k 一个可行的数字组合是一组正整数，
它们的和为n，且组合中的数字个数小于等于k, 组合中允许数字重复出现
输出：所有可能的组合数 (两个组合中出现的数字相同，顺序不同计为同一个）
'''


class Solution1:
    def __init__(self, k):
        self.res = [0 for _ in range(k)]
        self.res_num = 0
        self.p = 0
        self.k = k
        self.list_res = []

    def zhengshufenjie(self, n):
        if n <= 0:
            tmp = self.res[:self.p]
            tmp.sort()
            if tmp not in self.list_res:
                self.list_res.append(tmp)
                self.res_num += 1
                print(tmp)
        if self.p >= self.k:
            return
        for i in range(1, n + 1):
            self.res[self.p] = i
            self.p += 1
            self.zhengshufenjie(n - i)
            self.p -= 1


'''
给一个类似下面的字符串，字符串里有一些双括号括起的内容，并且给定一个字典，我们需要编写一段程序将括号以及括号里的内容替换为字典里映射的内容。
1. 如果字典里不存在需要的映射，则输出只是将括号去掉，括号里的内容原样保存。
2. 如果括号里的内容为空，则括号原样输出。
3. 匹配的时候以最短优先原则，比如有{{abcde{{fg}}，则取fg，而不取 abcde{{fg；比如{{a{{}}c}}则取中间的{{}}，则替换后结果还是{{a{{}}c}}。
4. 替换只会从左到右执行一遍。比如有{{abc}}, 字典 abc -> a{{b}}c，b -> c，则结果是a{{b}}c，不会对b再进行一次替换。
约束
    1.只允许使用语言提供的基本类库，标准类库(C++可以使用STL)
    2.不允许使用正则表达式来处理字符串
'''
'''
这是{{un{{it}}很长很长的句子。
1
unit->一个
'''
class Solution2():
    def tihuan(self, s, dic):
        stack = []
        # print(dic)
        i = 0
        while 1:
            if i > len(s) - 1:
                break
            if s[i] == '{' and s[i + 1] == '{':
                stack.append(i)
            if s[i] == '}' and s[i + 1] == '}':
                j = stack.pop(-1)
                print(i, j)
                if i - j != 2:
                    st = s[j + 2:i]
                    if st in dic:
                        s = s[:j] + dic[st] + s[i + 2:]
                    else:
                        s = s[:j] + st + s[i + 2:]
                        i = i + 2
                        # print(i)
                        i = i - len(st) - 4
                        continue
                    i = i + 2
                    # print(i)
                    i = i - len(st) - 4 + len(dic[st])
                    # print(s, i)
                    continue

            i += 1
        return s


'''
便利蜂手机 APP 由多个模块构成。模块更新时，可以指定依赖关系。若 A 模块依赖 B 模块，
则 B 模块更新后，A 模块才可以更新；如 A、B 模块相互依赖 ，则 A、B 需要同时更新。

求：计算某个模块的更新，需要依赖的其他模块数量。
如：给定模块依赖关系 A->B , B->C，则对于模块 A，依赖的模块数量为 2
A
3
A->B
B->C
C->A
'''
class Solution3():
    def __init__(self,mok):
        self.res_list=[]
        self.mok=mok

    def search_yilia(self, mok, dic):
        if mok not in dic:
            return 0

        for each in dic[dic[mok]]:
            if each==self.mok:
                continue
            if each not in self.res_list:
                self.res_list.append(each)
                self.search_yilia(each,dic)
        #print(self.res_list)
        return len(self.res_list)

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    s = Solution1(k)
    s.zhengshufenjie(n)
    print(s.res_num)

    # str = input()
    # n = int(input())
    # dic = {}
    # for _ in range(n):
    #     tmp = input().split('->')
    #     dic[tmp[0]] = tmp[1]
    # s = Solution2()
    # print(s.tihuan(str, dic))

    # mok = input()
    # num = int(input())
    # dic = {}
    # for _ in range(num):
    #     tmp = input().split('->')
    #     if tmp[0] not in dic:
    #         dic[tmp[0]]= tmp[1]
    #     else:
    #         dic[tmp[0]] = [dic[tmp[0]],tmp[1]]
    # s = Solution3(mok)
    # print(s.search_yilia(mok, dic))