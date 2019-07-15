'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1

示例 2:
输入:
11000
11000
00100
00011

输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def numIslands(self, grid):
        if not grid:
            return None
        m = len(grid)
        n = len(grid[0])
        num = 0
        def dfs(x,y):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == '0':
                return

            grid[x][y] = '0'

            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num += 1
                    dfs(i, j)

        return num

class Solution:
    def numIslands(self, grid):
        if not grid:
            return None
        m = len(grid)
        n = len(grid[0])
        numIsland = 0
        parent = [-1] * 7
        rank = [0] * 7

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                        numIsland += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] == '0'
                    if i - 1 >= 0 and grid[i-1][j] == '1':
                        if self.union(i-1, j):
                            numIsland -= 1
                    if i + 1 < m and grid[i+1][j] == '1':
                        if self.union(i+1, j):
                            numIsland -= 1

        return numIsland



    def find(self, cur, parent):
        cur_root = cur
        if parent[cur_root] != -1:
            cur_root = parent[cur_root]

        return cur_root

    #True:合并成功，无环；False：合并失败，有环。
    def union(self, x, y, parent, rank):
        x_root = self.find(x, parent)
        y_root = self.find(y, parent)

        if x_root != y_root:
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
# print(s.numIslands([["1","1","0","0","0"],
#                     ["1","1","0","0","0"],
#                     ["0","0","1","0","0"],
#                     ["0","0","0","1","1"]]
#                    ))

# print(s.numIslands([["1","1","1","1","0"],
#                     ["1","1","0","1","0"],
#                     ["1","1","0","0","0"],
#                     ["0","0","0","0","0"]]
#                    ))

print(s.numIslands([["1","0","1","1","0","1","1"]]))















