'''
二叉树的序列化和反序列化

二叉树被记录成文件的过程叫做序列化；
从文件重建二叉树的过程叫做反序列化。

同LeetCode297
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    '''------------------------前序遍历法----------------------'''
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#!'
        result = str(root.val) + '!'
        result += self.serialize(root.left)
        result += self.serialize(root.right)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print(data)
        queue = data.split('!')[:-1]
        return self.recon(queue)

    def recon(self, queue):
        value = queue.pop(0)
        if value == '#':
            return None
        root = TreeNode(int(value))
        root.left = self.recon(queue)
        root.right = self.recon(queue)
        return root

    '''------------------------层次遍历法----------------------'''
    def serialize(self, root):
        if not root:
            return '#!'
        result = str(root.val) + '!'
        queue = []
        queue.append(root)
        while queue:
            root = queue.pop(0)
            if root.left:
                result += str(root.left.val) + '!'
                queue.append(root.left)
            else:
                result += '#!'
            if root.right:
                result += str(root.right.val) + '!'
                queue.append(root.right)
            else:
                result += '#!'

        return result

root = TreeNode(12)
root.left = TreeNode(3)
root.right = None
root.left.left = None
root.left.right = None


codec = Codec()
x = codec.deserialize(codec.serialize(root))
print(x.val)