'''
在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。
这些字符会将方块划分为一些共边的区域。
（请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
返回区域的数目。

 
示例 1：
输入：
[" /","/ "]
输出：2

示例 2：
输入：
[" /","  "]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regions-cut-by-slashes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
把每个1X1方格按顺时针分成上0，右1，下2，左3四个三角形，将其视为节点。
若是\，则合并左下两个三角形；若是/，则合并上右两个三角形；若是空，则合并四个三角形。
'''


class Solution:
    def regionsBySlashes(self, grid):
        g = []
        for i in grid:
            g.extend(list(i))
        m = len(g)
        num = 4 * m
        parent = [-1] * 4 * m
        rank = [0] * 4 * m
        for i in range(len(grid)):
            for j in range(len(grid)):
                zero = 4 * (i * len(grid) + j)
                #各个小方块内部的联通
                if grid[i][j] == ' ':
                    if self.union(zero, zero + 1, parent, rank):
                        num -= 1
                    if self.union(zero+1, zero+2, parent, rank):
                        num -= 1
                    if self.union(zero+2, zero+3, parent, rank):
                        num -= 1

                elif grid[i][j] == '\\':
                    if self.union(zero, zero + 1, parent, rank):
                        num -= 1
                    if self.union(zero+2, zero+3, parent, rank):
                        num -= 1

                else:
                    if self.union(zero, zero + 3, parent, rank):
                        num -= 1
                    if self.union(zero+1, zero+2, parent, rank):
                        num -= 1
                #方块之间的联通
                if i > 0:
                    if self.union(zero, zero - 4 * len(grid) + 2, parent, rank):
                        num -= 1
                if j > 0:
                    if self.union(zero+3, zero-3, parent, rank):
                        num -= 1

        return num

    def find(self, x, parent):
        x_root = x
        while parent[x_root] != -1:
            x_root = parent[x_root]

        return x_root

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
print(s.regionsBySlashes(["\\/","/\\"]))