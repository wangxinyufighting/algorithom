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

class Solution(object):
    '''------------------递归---------------------'''
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
    def postorderTraversal(self, root):
        if not root:
            return None
        s1 = []
        s2 = []
        s1.append(root)
        result = []
        while s1:
            root = s1.pop()
            s2.append(root)
            if root.left:
                s1.append(root.left)
            if root.right:
                s1.append(root.right)

        while s2:
            result.append(s2.pop().val)

        return result




























