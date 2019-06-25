'''
二叉树的中序遍历

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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        result = []
        self.inorderTraversal_(root, result)
        return result

    def inorderTraversal_(self, node, result):
        if not node:
            return None
        self.inorderTraversal_(node.left, result)
        result.append(node.val)
        self.inorderTraversal_(node.right, result)

'''-----------------非递归--------------------'''