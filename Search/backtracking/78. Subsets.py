'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[[3],[1],  [2],  [1,2,3],  [1,3],  [2,3],  [1,2],  []]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res += [[i] + num for num in res]

    def subsets(self, nums):
        res = []
        n = len(nums)

        def helper(i, temp):
            print(temp)
            res.append(temp)
            for j in range(i, n):
                helper(j+1, temp+[nums[j]])

        helper(0, [])
        return res

    def subsets(self, nums):
        if not nums:
            return [[]]
        res = []
        for i in self.subsets(nums[1:]):
            res.append(i)
            res.append(nums[:1] + i)

        return res

class Solution:
    def subsets(self, nums):
        if not nums:
            return []
        result = []
        self.backtrack(0, nums, [], result)
        return result

    def backtrack(self,start, nums, temp, result):
        result.append(temp.copy())
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.backtrack(i+1, nums, temp, result)
            temp.pop()

s = Solution()
print(s.subsets([1,2,3]))
# for i in range(3,3):
#     print(i)

























