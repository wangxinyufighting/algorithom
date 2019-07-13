'''
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:
X X X X
X O O X
X X O X
X O X X

运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    '''
    超时
    '''
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None

        m = len(board)
        n = len(board[0])

        edges = []
        others = []
        all = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i == 0 or j == 0 or i == m-1 or j == n-1:
                        if (abs(i-1),j) not in edges and (i, abs(j-1)) not in edges:
                            edges.append((i, j))
                    else:
                        others.append((i, j))
                    all.append((i, j))

        result = []
        print(edges)
        def dfs(nodes):
            for start in edges:
                stack = [start]
                seen = set([start])
                while stack:
                    node = stack.pop()
                    for other in all:
                        if other not in seen:
                            if (other[0] == node[0] and abs(other[1] - node[1]) == 1) or \
                               (other[1] == node[1] and abs(other[0] - node[0]) == 1):
                                stack.append(other)
                                seen.add(other)
                    if node not in result:
                        result.append(node)

        dfs(edges)
        # print(result)
        for j in others:
            if j not in result:
                board[j[0]][j[1]] = 'X'


class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])

        if m < 3 or n < 3:
            return board

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or board[x][y] == 'X':
                return

            board[x][y] = '#'

            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)

        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

s = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = \
    [["O","X","X","O","X"],
 ["X","O","O","X","O"],
 ["X","O","X","O","X"],
 ["O","X","O","O","O"],
 ["X","X","O","X","O"]]
board = [["X","O","O","X","O","X","O"],
         ["O","X","X","X","X","X","O"]]
s.solve(board)
print(board)


'''
["X","X","X","X","X"],
["X","O","O","X","X"],
["X","X","O","X","X"],
["X","O","O","X"]


# [["O","X","X","O","X"],
#  ["X","O","O","X","O"],
#  ["X","O","X","O","X"],
#  ["O","X","O","O","O"],
#  ["X","X","O","X","O"]]

[['O', 'X', 'X', 'O', 'X'], 
['X', 'X', 'X', 'X', 'O'], 
['X', 'X', 'X', 'O', 'X'], 
['O', 'X', 'O', 'O', 'O'], 
['X', 'X', 'O', 'X', 'O']]
'''








