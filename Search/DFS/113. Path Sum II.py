'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
DFS+回溯
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum):
        if not root:
            return []

        result = []
        def trackback(node, sum, temp):
            if not node:
                return
            if not node.left and not node.right and sum - node.val == 0:
                temp += [node.val]
                result.append(temp)
                return

            trackback(node.left, sum - node.val, temp + [node.val])
            trackback(node.right, sum - node.val, temp + [node.val])

        trackback(root, sum, [])
        return result


s = Solution()
root = TreeNode(5)
node1 = TreeNode(4)
node2 = TreeNode(8)
node3 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node11 = TreeNode(5)
node12 = TreeNode(1)
root.left = node1
root.right = node2
node1.left = node3
node2.left = node5
node2.right = node6
node3.left = node7
node3.right = node8
node6.right = node12
node6.left = node11

# root = TreeNode(1)
# node1 = TreeNode(-2)
# node2 = TreeNode(-3)
# node3 = TreeNode(1)
# node4 = TreeNode(3)
# node5 = TreeNode(-2)
# node6 = TreeNode(4)
# node7 = TreeNode(7)
# node8 = TreeNode(-1)
# node11 = TreeNode(5)
# node12 = TreeNode(1)
# root.left = node1
# root.right = node2
# node1.left = node3
# node1.right = node4
# node2.left = node5
# # node2.right = node6
# node3.left = node8


print(s.pathSum(root, 22))
