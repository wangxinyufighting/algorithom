'''
给定一个二叉树，返回所有从根节点到叶子节点的路径。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if not root:
            return []
        result = []

        def backtrack(node, temp):
            if not node:
                return
            if not node.left and not node.right:
                if temp:
                    temp += '->' + str(node.val)
                else:
                    temp += str(node.val)
                result.append(temp)

            if temp:
                backtrack(node.left, temp + '->' + str(node.val))
                backtrack(node.right, temp + '->' + str(node.val))
            else:
                backtrack(node.left, temp + str(node.val))
                backtrack(node.right, temp + str(node.val))

        backtrack(root, '')
        return result
