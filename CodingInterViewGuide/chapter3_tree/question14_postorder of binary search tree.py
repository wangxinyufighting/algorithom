'''
基础：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
进阶：根据后序遍历构造二叉搜索树

牛客：https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd?tpId=13&tqId=11176&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
leetcode相关的题目：
98.验证二叉搜索树 https://leetcode-cn.com/problems/validate-binary-search-tree/
109：有序链表转换二叉搜索树 https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/
1008. 先序遍历构造二叉搜索树 https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''基础：判断是否是二叉搜索树'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        return self.isPost(sequence, 0, len(sequence)-1)

    def isPost(self, sequence, start, end):
        if start == end:
            return True

        less = -1
        more = end

        for i in range(start, end):
            if sequence[end] > sequence[i]:
                less = i
            else:
                more = i if more == end else more

        if less == -1 or more == end:
            return self.isPost(sequence, start, end-1)

        if less != more-1:
            return False

        return self.isPost(sequence, start, less) and self.isPost(sequence, more, end-1)

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

s = Solution()
print(s.bstFromPreorder([8,5,1,7,10,12]))





