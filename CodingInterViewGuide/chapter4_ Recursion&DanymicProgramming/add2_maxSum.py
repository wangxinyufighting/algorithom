'''
给定nums, 如[1，2，5，6，3，9]
选择几个元素，要求和最大。要求不能选择相邻的元素
'''

def maxSum(nums):
    opt = [0]*len(nums)
    opt[0] = nums[0]
    opt[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        opt[i] = max(opt[i-1], opt[i-2]+nums[i])

    return opt[-1]


print(maxSum([1, 2, 4, 1, 7, 8, 3]))