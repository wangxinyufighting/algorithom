'''
用递归和非递归前中后序遍历二叉树
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#先序遍历 同LeetCode144
#递归
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        result = []
        self.preorderTraversal_(root, result)
        return result

    def preorderTraversal_(self, node, result):
        if not node:
            return None
        result.append(node.val)
        self.preorderTraversal_(node.left, result)
        self.preorderTraversal_(node.right, result)

