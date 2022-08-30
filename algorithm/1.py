class Solution:
    def twoSum(self, nums, target):
        l= len(nums)
        i = 0
        while i < l:
            try:
                index=nums.index(target-nums[i])
            except:
                i+=1
                continue
            if index!=i:
                return [i,index]
            i+=1
        return []

class Solution2:
    def twoSum(self,nums,target):
        dic={}
        for index,value in enumerate(nums):
            tar=target-value
            if tar in dic:
                return [index,dic[tar]]
            else:
                dic[value]=index

if __name__=='__main__':
    s=Solution2()
    
    print(s.twoSum([3,2,3], 6))