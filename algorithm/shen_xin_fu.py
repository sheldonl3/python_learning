class Solution:
    def get_repeated_chars(self, str_a, strb):
        # l1,l2=len(str1),len(str2)
        res = ''
        for each in strb:
            if each in str_a:
                if each not in res:
                    res += each
                else:
                    continue
        return res


class Solution2:
    def largest_perimeter(self, arry):
        arry = sorted(arry)
        l = len(arry)
        if l < 3:
            return 0
        for i in range(l - 1, 1, -1):
            if arry[i - 1] + arry[i - 2] > arry[i]:
                return arry[i - 1] + arry[i - 2] + arry[i]
        return 0


class Solution3:
    def __init__(self):
        self.cnt = 65535

    def min_send(self, nums, m):
        nums = [0] + nums
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        idx = [i for i in range(m + 1)]
        idx[m] = len(nums) - 1
        self.backtrace(nums, idx)
        return self.cnt

    def backtrace(self, arr, idx):
        maxx = arr[idx[0]]
        for i in range(1, len(idx)):
            maxx = max(maxx, arr[idx[i]] - arr[idx[i - 1]])
        self.cnt = min(self.cnt, maxx)
        for i in range(1, len(idx)):
            if i + 1 < len(idx) and idx[i + 1] - idx[i] == 1:
                continue
            if idx[i] == len(arr) - 1:
                continue
            idx[i] += 1
            self.backtrace(arr, idx)
            idx[i] -= 1


class Solution4:
    def min_send(self, nums, m):

        def backtrace(nums, m, sum, len):
            l = len(nums)
            if l == 1:
                return nums[0],1
            i = 1
            while i < l - m:
                tmp_sum, tmp_len = backtrace(nums[i:], m - 1, sum, len)
                if tmp_sum > sum:
                    len = tmp_len
                    
                i += 1
            return

        res, _ = backtrace(nums, m, 0, 0)
        return sum


if __name__ == '__main__':
    # s=Solution()
    # a=input().replace('"','')
    # a=a.split(',')
    # print(s.get_repeated_chars(a[0],a[1]))
    s = Solution4()
    print(s.min_send([4, 3, 5, 10, 12], 2))
