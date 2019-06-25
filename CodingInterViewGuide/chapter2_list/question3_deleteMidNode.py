'''
基本：
1、删除中间节点
1-2       删除1
1-2-3     删除2
1-2-3-4   删除2
1-2-3-4-5 删除3

进阶：
2、删除a/b处的节点
1-2-3-4-5 a/b值为r
a/b in [0,1/5]    删除1
a/b in (1/5,2/5]  删除2
a/b in (2/5,3/5]  删除3
a/b in (3/5,4/5]  删除4
a/b in (4/5,1]    删除5
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, head):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not head:
            return None

        if not head.next.next:
            head = head.next

        pre = head
        cur = head.next.next
        while cur.next and cur.next.next:
            pre = pre.next
            cur = cur.next.next

        pre.next = pre.next.next

        return head


    def deleteNode(self, head, a, b):
        # write your code here
        if not head or a < 1 or b < a:
            return None
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        r = int((n * a) / b)

        if r == 1:
            head = head.next

        if r > 1:
            cur = head
            r -= 1
            while r != 1:
                cur = cur.next
                r -= 1
            cur.next = cur.next.next

        return head