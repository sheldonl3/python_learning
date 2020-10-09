'''
数组中查找和为target的所有组合方式
'''

res = []


def find_sort(nums, target, tmp):
    l = len(nums)
    if l == 1:
        if nums[0] == target:
            lis = sorted(nums + tmp)
            if lis not in res:
                res.append(lis)
            return
    for i in range(l):
        if nums[i] > target:
            continue
        elif nums[i] == target:
            lis = sorted([nums[i]] + tmp)
            if lis not in res:
                res.append(lis)
                continue
        else:
            find_sort(nums[i + 1:], target - nums[i], tmp + [nums[i]])


if __name__ == '__main__':
    find_sort([1, 3, 5, 8, 7, 4, 1, 4], 8, [])
    print(res)
