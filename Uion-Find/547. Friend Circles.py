'''
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。
如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。
你必须输出所有学生中的已知的朋友圈总数。

示例 1:

输入:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。
示例 2:

输入:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出: 1
说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/friend-circles
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


#标准的并查集问题，找到形成环的个数
class Solution:
    def findCircleNum(self, M):
        num = len(M)
        parent = [-1] * len(M)
        rank = [0] * len(M)
        for i in range(len(M)):
            for j in range(len(M)):
                if i != j and M[i][j] == 1:
                    # 合并一次，就意味着朋友圈减少一个
                    if self.union(i, j, parent, rank):
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
            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1
            return True
        else:
            return False


s = Solution()
print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
# print(s.findCircleNum([[1,1,0],[1,1,1],[0,1,1]]))




















