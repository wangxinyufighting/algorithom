'''
删除倒数第K个节点
同LeetCode 19
要记住，删除node的重点是找到需要被删除的前一个node
然后使用 node.next = node.next.next删除
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or n < 1:
            return None

        cur = head
        while cur:
            n -= 1
            cur = cur.next

        if n == 0:
            head = head.next

        if n < 0:
            cur = head
            n += 1
            while n != 0:
                n += 1
                cur = cur.next
            cur.next = cur.next.next

        return head

head = ListNode(1)
node1 = ListNode(2)
head.next = node1
node2 = ListNode(3)
node1.next = node2
node3 = ListNode(4)
node2.next = node3
node4 = ListNode(5)
node3.next = node4

s = Solution()
x = s.removeNthFromEnd(head, 2)
while x:
    print(x.val)
    x = x.next