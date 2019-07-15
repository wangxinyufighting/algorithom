'''
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[[2],[1],[1,2,2],[2,2],[1,2],[]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return []

        result = []
        nums.sort()
        self.backtrack(0, [], nums, result)
        return result

    def backtrack(self, start, temp, nums, result):
        result.append(temp.copy())
        for i in range(start, len(nums)):
            #跳过重复的元素
            if i > start and nums[i-1] == nums[i]:
                continue
            temp.append(nums[i])
            self.backtrack(i+1, temp, nums, result)
            temp.pop()

s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
