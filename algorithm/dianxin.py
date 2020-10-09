def choushu(num):
    a, b, c = 0, 0, 0
    dp = [1 for _ in range(num)]
    # print(dp)
    for i in range(1, num):
        dp[i] = min(dp[a] * 2, min(dp[b] * 3, dp[c] * 5))
        if dp[i] == dp[a] * 2:
            a += 1
        if dp[i] == dp[b] * 3:
            b += 1
        if dp[i] == dp[c] * 5:
            c += 1
    return dp[-1]


def delete_string(str):
    if str == None:
        return
    dic = {}
    for each in str:
        if each in dic:
            dic[each] += 1
        else:
            dic[each] = 1
    min_num = (sorted(dic.items(), key=lambda item: item[1]))[0][1]
    # print(min_num)
    res = ''
    # print(dic)
    for each in str:
        if dic[each] == min_num:
            continue
        else:
            res += each
    return res


class SmallStack:
    def __init__(self):
        self.stack = []
        self.small_stack = []

    def push(self, num):
        self.stack.append(num)
        if not self.small_stack or num <= self.small_stack[-1]:
            self.small_stack.append(num)

    def pop(self):
        if self.stack.pop() == self.small_stack[-1]:
            self.small_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.small_stack[-1]


if __name__ == "__main__":
    # n = int(input())
    # print(choushu(n))

    # str = input()
    # print(delete_string(str))
    s = SmallStack()
    num = int(input())
    for _ in range(num):
        do = input().split()
        # print(do)
        if len(do) == 2:
            s.push(int(do[1]))
        else:
            if do[0] == 'getMin':
                print(s.getMin())
            elif do[0] == 'pop':
                s.pop()
            else:
                print(s.top())
