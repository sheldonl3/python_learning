class Solution:
    def findKthLargest(self, nums, k):
        l = len(nums)

        def tiaozheng(nums, index):  # 调整谁,到l; l后面会减少，不再调整已经排好序的部分
            left = index * 2 + 1
            right = index * 2 + 2
            if right < l:
                max_num = max(nums[left], nums[right])
                if max_num == nums[left]:
                    mi = left
                else:
                    mi = right
            elif left < l:
                max_num = nums[left]
                mi = left
            else:
                return
            if max_num > nums[index]:
                nums[index], nums[mi] = nums[mi], nums[index]
                tiaozheng(nums, mi)  # 递归调整

        def make_heap(nums):  # 建大顶堆
            if l < 2:
                return nums
            for i in range(l // 2, -1, -1):  # 从最下面的非叶子节点调整
                tiaozheng(nums, i)

        if l < k:
            return -1
        make_heap(nums)
        print(nums)
        #for i in range(l):
        while l>0:
            nums[0], nums[l - 1] = nums[l - 1], nums[0]
            l = l - 1
            tiaozheng(nums, 0)
        print(nums)
        return nums[l]


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([2, 1,5,56,42,31,78,6546], 2))
