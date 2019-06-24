'''
判断回文数
LeetCode9
https://leetcode-cn.com/problems/palindrome-number/

本题与LeetCode9不同的是，
本题把-121 当做是回文数
LeetCode9严格按照回文，认为-121不是回文数
'''
class Solution(object):
    #按照LeetCode9的要求
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        help = 1
        while x / help >= 10:
            help *= 10

        while x != 0:
            if x%10 != x/help:
                return False
            x = (x % help) / 10
            help /= 100

        return True

    #按照本文的要求：
    def isPalindrome(self, x):
        x = x if x >= 0 else -x
        help = 1
        while x/help >= 10:
            help *= 10

        while x != 0:
            if x%10 != x/help:
                return False

            x = (x % help) / 10
            help /= 100

        return True

    