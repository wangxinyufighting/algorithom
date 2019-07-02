# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        #         if not root:
        #             return 0

        #         if not root.left and not root.right:
        #             return 1

        #         minD = 10000000
        #         if root.left:
        #             minD = min(self.minDepth(root.left), minD)
        #         if root.right:
        #             minD = min(self.minDepth(root.right), minD)

        #         return minD + 1

        if root is None:
            return 0
        stack = [(1, root)]
        while stack:
            n_height, node = stack.pop(0)
            if node:
                if not node.right and not node.left:
                    return n_height
                stack.append((n_height + 1, node.right))
                stack.append((n_height + 1, node.left))

        return n_height
