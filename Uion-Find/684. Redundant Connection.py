'''
在本问题中, 树指的是一个连通且无环的无向图。

输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。

返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

示例 1：

输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/redundant-connection
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#标准的并查集问题，找到形成环的边，然后输出
class Solution:
    def findRedundantConnection(self, edges):
        nodesNum = len(set([j for i in edges for j in i]))
        parent = [-1] * nodesNum
        rank = [-1] * nodesNum
        result = []
        for edge in edges:
            if not self.union(edge[0]-1, edge[1]-1, parent, rank):
                result.append(edge)
        if result:
            return result[-1]
        else:
            return None

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
print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))















