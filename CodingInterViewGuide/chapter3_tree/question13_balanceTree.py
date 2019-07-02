'''
判断二叉树是否是平衡树

平衡即任何节点的左右子树高度差不超过1
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isB(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = self.isB(root.left)
        right = self.isB(root.right)

        if left < 0 or right < 0:
            return -1

        if abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if self.isB(root) == -1:
            return False
        else:
            return True

root = TreeNode(1)
l1_1 = TreeNode(2)
l1_2 = TreeNode(2)
l2_1 = TreeNode(3)
l2_2 = TreeNode(3)
l3_1 = TreeNode(4)
l3_2 = TreeNode(4)
root.left = l1_1
root.right = l1_2
l1_1.left =l2_1
l1_1.right = l2_2
l2_1.left = l3_1
l2_1.right = l3_2
l2_2.left = None
l2_2.right = None

# s = Solution()
# print(s.isBalanced(root))
x = [1,2,3,4]
x.index()
