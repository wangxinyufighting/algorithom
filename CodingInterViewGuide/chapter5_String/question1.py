'''
判断两个字符串是不是互为变形词
变形词即为出现的字符类型一样，且次数一样
如"abc"和"cba"
同LintCode211：https://www.lintcode.com/problem/string-permutation/description
'''
class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        if len(A) != len(B):
            return False
        map = {}
        for i in A:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
        for i in B:
            map[i] -= 1
            if map[i] < 0:
                return False

        return True