'''
判断一棵树是否是搜索二叉树和完全二叉树
完全二叉树：leetcode 958 https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        q = [root]
        leaf = False
        while q:
            node = q.pop(0)
            l = node.left
            r = node.right

            if (leaf and (l or r)) or (not l and r):
                return False

            if l:
                q.append(l)
            if r:
                q.append(r)
            if not r or not l:
                leaf = True

        return True