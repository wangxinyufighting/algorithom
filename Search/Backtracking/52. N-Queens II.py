'''
N皇后问题，输出方案的个数
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 0
        return len(self.queen(n))

    def conflict(self, current, arranged):
        length = len(arranged)
        flag = False
        for i in range(length):
            if abs(current - int(arranged[i])) in (0, length - i):
                flag = True
                break

        return flag

    def queen(self, n):
        result = []

        def backtrack(arranged):
            if len(arranged) == n:
                result.append(arranged)
                return

            for i in range(n):
                if not self.conflict(i, arranged):
                    backtrack(arranged + str(i))

        backtrack('')
        return result