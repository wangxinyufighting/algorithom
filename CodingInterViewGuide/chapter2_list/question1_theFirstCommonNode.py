'''
打印两个链表公共的部分

'''

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return None

        while l1 and l2:
            if l1.val > l2.val:
                l2 = l2.next
            elif l1.val < l2.val:
                l1 = l2.next
            else:
                print(l1.val)
                l1 = l1.next
                l2 = l2.next