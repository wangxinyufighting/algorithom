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
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#这个题找到和边界联通的O就行了，剩下的O替换成X
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
                    Os.append((i,j))

        parent = [-1] * len(Os)
        rank = [0] * len(Os)
        result = []
        for i in Os:
            for j in Os:
                if i != j:
                    # if i[0] == 0 or i[1] == 0 or j[0] == 0 or j[1] == 0 \
                    #     or i[0] == m-1 or i[1] == n-1 or j[0] == m-1 or j[1] == n-1:
                    #     print(i, j)
                    if self.union(Os.index(i), Os.index(j), parent, rank, Os, m, n):
                        if i not in result:
                            result.append(i)
                        if j not in result:
                            result.append(j)

        print(result)
        flag = True
        if result:
            for i in result:
                if i[0] == 0 or i[1] == 0 or i[0] == len(board)-1 or i[1] == len(board[0])-1:
                    flag = False

            if flag:
                for i in result:
                    board[i[0]][i[1]] = 'X'
        else:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == 'O':
                        if i != 0 and j != 0 and i != len(board)-1 and j != len(board[0])-1:
                            board[i][j] = 'X'

    def find(self, x, parent):
        x_root = x
        while parent[x_root] != -1:
            x_root = parent[x_root]

        return x_root

    def union(self, x, y, parent, rank, Os, m, n):
        x_root = self.find(x, parent)
        y_root = self.find(y, parent)

        if x_root != y_root:
            # if Os[x_root][0] == 0 or Os[x_root][1] == 0 or Os[x_root][0] == m-1 or Os[x_root][1] == n-1:
            #     parent[y_root] = x_root
            #     return True
            # elif Os[y_root][0] == 0 or Os[y_root][1] == 0 or Os[y_root][0] == m-1 or Os[y_root][1] == n-1:
            #     parent[x_root] = y_root
            #     return True
            # else:
            #     return False
            if rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            elif rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            else:
                parent[x_root] = y_root
                rank[y_root] += 1
            return True
        else:
            return False

s = Solution()
test = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# test = [["X","X","X"],["X","O","X"],["X","X","X"]]
# test = [["O","X","O"],["X","O","X"],["O","X","O"]]
# test = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
# test = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
x = s.solve(test)
print(test)
# [["X","X","X","X"],
#  ["X","O","O","X"],
#  ["X","X","O","X"],
#  ["X","O","X","X"]]
#
# [["X","X","X","X"],
#  ["X","X","O","X"],
#  ["X","X","O","X"],
#  ["X","X","X","X"]]
#
# [["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","O","X","X"]]

# [["X","O","X","O","X","O"],
#  ["O","X","O","X","O","X"],
#  ["X","O","X","O","X","O"],
#  ["O","X","O","X","O","X"]]
#
# [["O","X","X","O","X"],
#  ["X","O","O","X","O"],
#  ["X","O","X","O","X"],
#  ["O","X","O","O","O"],
#  ["X","X","O","X","O"]]
#
# [["O","X","X","O","X"],
#  ["X","O","O","X","O"],
#  ["X","O","X","O","X"],
#  ["O","X","O","O","O"],
#  ["X","X","O","X","O"]]




















