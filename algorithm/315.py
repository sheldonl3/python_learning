class Solution:
    def countSmaller(self, nums):#归并排序方法
        res = [0] * len(nums)
        if len(nums) < 1:
            return res
        arr = []
        for index, value in enumerate(nums):
            arr.append((index, value))  #有之前index的待排序数组

        def mersort(nums):
            if len(nums) < 2:
                return nums
            mid = len(nums) // 2
            left, right = nums[:mid], nums[mid:]
            return mer(mersort(left), mersort(right))

        def mer(left, right):
            print(left)
            print(right)
            tmp = []
            r = 0
            l = 0
            while l < len(left) and r < len(right):
                print(left,l,right,r)
                if left[l][1] <= right[r][1]:
                    tmp.append(left[l])
                    res[left[l][0]] += r  #key:归并左边的数据时候，左边要比右面数组中大r个，记录到res中
                    l += 1
                else:
                    tmp.append(right[r])
                    r += 1

            while l < len(left):
                tmp.append(left[l])
                res[left[l][0]] += r
                l += 1
            while r < len(right):
                tmp.append(right[r])
                r += 1
            return tmp

        mersort(arr)
        print(res)
        return res


if __name__ == '__main__':
    s = Solution()
    s.countSmaller([-1,0])
