'''
反转单链表和双链表
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class DoubleListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.last = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        pre = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre

    def reverseDoubleList(self, head):
        pre = None
        while head:
            next = head.next
            head.next = pre
            head.last = next
            pre = head
            head = next
        return pre