'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。解集不能包含重复的组合。 

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[[7],[2,2,3]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def combinationSum(self, candidates, target):
        n = len(candidates)
        if not candidates:
            return []

        result = []
        def backtrack(i, temp, sum):
            if sum > target or i == n:
                return

            if sum == target:
                result.append(temp)
                return

            backtrack(i, temp + [candidates[i]], sum + candidates[i])
            backtrack(i+1, temp, sum)

        backtrack(0, [], 0)
        return result

    def combinationSum1(self, candidates, target):
        n = len(candidates)
        if not candidates:
            return []

        result = []
        def backtrack(i, temp, sum):
            if sum == target:
                result.append(temp)
                return

            for i in range(i, n):
                if sum > target or i == n:
                    return
                backtrack(i, temp + [candidates[i]], sum + candidates[i])

        backtrack(0, [], 0)
        return result

s = Solution()
print(s.combinationSum1([2,3,6,7],7))

        