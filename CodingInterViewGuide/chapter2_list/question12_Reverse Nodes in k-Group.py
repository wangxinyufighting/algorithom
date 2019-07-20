'''
同leetcode25

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''方法一：使用栈。O(N),O(K)'''
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k < 2:
            return head

        stack = []
        newhead = head
        pre = None
        cur = head

        while cur:
            next = cur.next
            stack.push(cur)
            if len(stack) == k:
                pre = self.reverse(stack, pre, next)
                newhead = cur if newhead == head else newhead
            cur = next
        return newhead

    def reverse(self, stack, left, right):
        cur = stack.pop()
        if left:
            left.next = cur

        while stack:
            next = stack.pop()
            cur.next = next
            cur = next

        cur.next = right
        return cur

    '''方法一：不使用栈。O(N),O(1)'''
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k < 2:
            return head
        cur = head
        pre = None
        count = 1
        while cur:
            next = cur.next
            if count == k:
                start = pre.next if pre else head
                head = cur if pre else head
                self.resign(pre, start, cur, next)
                pre = start
                count = 0

            count += 1
            cur = next
        return head

    def resign(self, left, start, end, right):
        pre = start
        cur = start.next
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        if left:
            left.next = end
        start.next = right


s = Solution()
s.reverseKGroup(None, 3)


























