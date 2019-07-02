'''
通过有序数组生成二叉平衡树
该数组是所生成的二叉平衡树的中序遍历
同leetcode108. 将有序数组转换为二叉搜索树 https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/submissions/

相关：
109：有序链表转换二叉搜索树 https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/
1008. 先序遍历构造二叉搜索树 https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''最好再写个非递归的解法'''
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        return self.conTree(nums, 0, len(nums) - 1)

    def conTree(self, nums, start, end):
        if start > end:
            return None

        mid = int((start + end) / 2)
        root = TreeNode(nums[mid])
        root.left = self.conTree(nums, start, mid - 1)
        root.right = self.conTree(nums, mid + 1, end)

        return root

'''先序遍历构造二叉搜索树'''
class Solution:
    def bstFromPreorder(self, preorder):
        return self.bst(preorder, 0, len(preorder) - 1)

    def bst(self, preorder, start, end):
        if start > end:
            return None

        root = TreeNode(preorder[start])

        for i in range(start, end + 1):
            if preorder[i] > preorder[start]:
                root.left = self.bst(preorder, start + 1, i - 1)
                root.right = self.bst(preorder, i, end)
                return root

        root.left = self.bst(preorder, start + 1, end)
        return root