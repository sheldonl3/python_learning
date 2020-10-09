class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def huisu(numlist, lis):
            # print(numlist, lis)
            if numlist == '':
                return False
            res = False
            if numlist[0] == '0':
                if len(numlist) == 1:
                    return 0 == lis[-1] + lis[-2]
                res |= huisu(numlist[1:], lis + [0])
            else:
                for i in range(len(numlist)):
                    if len(lis) >= 2:
                        if int(numlist[:i + 1]) == lis[-1] + lis[-2]:
                            if i == len(numlist) - 1:
                                # print('TTT', numlist, lis)
                                return True
                            else:
                                res |= huisu(numlist[i + 1:], lis + [int(numlist[:i + 1])])
                    else:
                        res |= huisu(numlist[i + 1:], lis + [int(numlist[:i + 1])])
            return res

        res = False
        for i in range(len(num) - 2):
            if num[0] == '0':
                res |= huisu(num[1:], [0])
                break
            res |= huisu(num[i + 1:], [int(num[:i + 1])])
            # print('ddd')
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.isAdditiveNumber('199100199'))
