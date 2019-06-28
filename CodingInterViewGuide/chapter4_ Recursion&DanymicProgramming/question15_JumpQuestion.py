'''
跳跃游戏 P235
同LeetCode45

给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    输入: [2,3,1,1,4]
    输出: 2
    解释: 跳到最后一个位置的最小跳跃数是 2。
         从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return None
        #需要跳跃的步数
        jump = 0
        #跳jump步可以到达的最远位置
        cur = 0
        #跳jump+1步可以到达的最远位置
        next = 0

        for i in range(len(nums)):
            if cur < i:
                jump += 1
                cur = next
            next = max(next, i + nums[i])

        return jump

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not nums:
        return None




# print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))

