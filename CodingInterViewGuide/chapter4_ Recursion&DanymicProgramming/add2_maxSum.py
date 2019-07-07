'''
给定nums, 如[1，2，5，6，3，9]
选择几个元素，要求和最大。要求不能选择相邻的元素

同leetcode198 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def maxSum(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    f = [0] * len(nums)
    f[0] = nums[0]
    f[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        f[i] = max(f[i - 1], f[i - 2] + nums[i])

    return f[-1]


print(maxSum([1, 2, 4, 1, 7, 8, 3]))