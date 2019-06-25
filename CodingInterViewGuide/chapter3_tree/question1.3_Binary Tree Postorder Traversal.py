'''
二叉树的后序遍历

同LeetCode94
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/submissions/
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''------------------递归---------------------'''
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        result = []
        self.postorderTraversal_(root, result)
        return result

    def postorderTraversal_(self, node, result):
        if not node:
            return None
        self.postorderTraversal_(node.left, result)
        self.postorderTraversal_(node.right, result)
        result.append(node.val)

'''-----------------非递归--------------------'''