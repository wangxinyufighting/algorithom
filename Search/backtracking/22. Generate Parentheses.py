'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def backtrack(temp, left, right):
            if len(temp) == n*2:
                result.append(temp)
                return

            if left < n:
                backtrack(temp + '(', left + 1, right)
            if left > right:
                backtrack(temp + ')', left, right + 1)

        backtrack('', 0, 0)
        return result

s = Solution()
print(s.generateParenthesis(2))

