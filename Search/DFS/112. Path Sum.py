'''
https://leetcode-cn.com/problems/path-sum/
给定一棵树，和数值k。若存在从根到某叶子节点的路径，其所有节点值的和为k，则返回True；否则返回False。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    递归1
    '''
    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:
            return 0 == sum
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
    '''
    递归2（回溯）
    '''

    def hasPathSum2(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and sum - root.val == 0:
            return True
        return self.hasPathSum2(root.left, sum - root.val) or self.hasPathSum2(root.right, sum - root.val)
    '''
    迭代
    '''
    def hasPathSum3(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        stack = [(root, sum - root.val)]
        while stack:
            node, cursum = stack.pop()
            if not node.left and not node.right and cursum == 0:
                return True
            if node.right:
                stack.append((node.right, cursum-node.right.val))
            if node.left:
                stack.append((node.left, cursum-node.left.val))

        return False

s = Solution()
root = TreeNode(5)
node1 = TreeNode(4)
node2 = TreeNode(8)
node3 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node12 = TreeNode(1)
root.left = node1
root.right = node2
node1.left = node3
node2.left = node5
node2.right = node6
node3.left = node7
node3.right = node8
node6.right = node12

print(s.hasPathSum2(root, 22))


