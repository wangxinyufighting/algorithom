'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def combinationSum2(self, candidates, target):
        if not candidates:
            return []

        result = []
        candidates.sort()

        def backtrack(i, temp, sum):
            if sum == target:
                result.append(temp)
                return

            if len(temp) == len(candidates) or sum > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j-1] == candidates[j]:
                    continue
                backtrack(j + 1, temp + [candidates[j]], sum + candidates[j])

        backtrack(0, [], 0)
        return result

s = Solution()
print(s.combinationSum2([2,5,2,1,2], 5))