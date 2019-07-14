'''
5128. 最深叶节点的最近公共祖先
给你一个有根节点的二叉树，找到它最深的叶节点的最近公共祖先。
示例 1：
输入：root = [1,2,3]
输出：[1,2,3]

示例 2：
输入：root = [1,2,3,4]
输出：[4]

示例 3：
输入：root = [1,2,3,4,5]
输出：[2,4,5]
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:

        def maxDepth(node):
            if not node:
                return 0

            return max(maxDepth(node.left), maxDepth(node.right)) + 1

        depthR = maxDepth(root.right)
        depthL = maxDepth(root.left)

        if depthR == depthL:
            return root
        elif depthR > depthL:
            if depthR == 1:
                return root
            return self.lcaDeepestLeaves(root.right)
        elif depthR < depthL:
            if depthL == 1:
                return root
            return self.lcaDeepestLeaves(root.left)







s = Solution()

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)

root.left = node1
root.right = node2
node1.left = node3
# node1.right = node4
# node2.left = node5

print(s.lcaDeepestLeaves(root).val)



























