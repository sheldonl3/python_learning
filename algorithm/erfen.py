def erfen(nums):
    l = len(nums)
    if l <= 1:
        return 0
    left = 0
    right = l - 1
    while left < right:
        mid = (left + right) // 2
        if mid + 1 < l and nums[mid] > nums[mid + 1]:
            return mid + 1
        if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
            return mid
        if nums[mid] > nums[left]:
            left = mid + 1
        elif nums[mid] < nums[left]:
            right = mid - 1
        else:
            left += 1
    return left


if __name__ == '__main__':
    print(erfen([9, 10, 11, 11, 2, 4, 5]))
