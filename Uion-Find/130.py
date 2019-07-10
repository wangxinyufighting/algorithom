class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Os = []
        m = len(board)
        n = len(board[0])
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    Os.append((i, j))
        # print(Os)
        result = []
        # for i in Os:
        #     if i[0] == 0 or i[1] == 0 or i[0] == m - 1 or i[1] == n - 1:
        #         if (i[0]+1, i[1]) in Os:
        #             result.append((i[0]+1, i[1]))
        #             result.append(i)
        #         elif (i[0]-1, i[1]) in Os:
        #             result.append((i[0]-1, i[1]))
        #             result.append(i)
        #         elif (i[0], i[1]+1) in Os:
        #             result.append((i[0], i[1]+1))
        #             result.append(i)
        #         elif (i[0], i[1]-1) in Os:
        #             result.append((i[0], i[1]-1))
        #             result.append(i)


        for i in Os:
            if i[0] == 0 or i[1] == 0 or i[0] == m - 1 or i[1] == n - 1:
                result = self.find(i, Os, result, m, n)

        print(set(result))
    def find(self, i, Os, result, m, n):
        if (i[0] + 1, i[1]) in Os:
            result.append((i[0] + 1, i[1]))
            result.append(i)
            self.find((i[0] + 1, i[1]), Os, result, m, n)
        elif (i[0] - 1, i[1]) in Os:
            result.append((i[0] - 1, i[1]))
            result.append(i)
            self.find((i[0] - 1, i[1]), Os, result, m, n)
        elif (i[0], i[1] + 1) in Os:
            result.append((i[0], i[1] + 1))
            result.append(i)
            self.find((i[0], i[1] + 1), Os, result, m, n)
        elif (i[0], i[1] - 1) in Os:
            result.append((i[0], i[1] - 1))
            result.append(i)
            self.find((i[0], i[1] - 1), Os, result, m, n)
        return result

s = Solution()
test = [["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["O","O","O","X"]]
# test = [["X","X","X"],["X","O","X"],["X","X","X"]]
# test = [["O","X","O"],["X","O","X"],["O","X","O"]]
# test = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
# test = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
x = s.solve(test)