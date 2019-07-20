'''
同Leetcode239
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k < 1:
            return []
        result = []
        qmax = []
        index = 0
        for i in range(len(nums)):
            while qmax and nums[qmax[-1]] <= nums[i]:
                qmax.pop()
            qmax.append(i)
            if qmax[0] == i - k:
                qmax.pop(0)

            if i >= k-1:
                result.append(nums[qmax[0]])

        return result

s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


