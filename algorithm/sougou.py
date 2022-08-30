'''
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回一行字符串，表示原文。
# @param s1 string字符串一维数组 N*N的01矩阵，表示解密纸，0表示透明，1表示涂黑
# @param s2 string字符串一维数组 字符矩阵，表示密文
# @return string字符串
#
'''


class Solution:
    def __init__(self):
        self.res = ''

    def rotatePassword(self, s1, s2):
        res = ""
        lis = []
        m, n = len(s1), len(s1)
        if m == 0 or n == 0:
            return res
        for i in range(m):
            for j in range(n):
                if s1[i][j] == '0':
                    self.res += s2[i][j]
                    lis.append([i, j])

        def round(lis):
            for i in range(len(lis)):
                tuple = lis.pop(0)
                tuple_new = [tuple[1], m - 1 - tuple[0]]
                lis.append(tuple_new)
            lis = sorted(lis)
            for each in lis:
                self.res += s2[each[0]][each[1]]
            return lis

        lis = round(lis)
        lis = round(lis)
        round(lis)

        return self.res


if __name__ == '__main__':
    s = Solution()
    print(s.rotatePassword(["1101", "1010", "1111", "1110"], ["ABCD", "EFGH", "IJKL", "MNPQ"]))
