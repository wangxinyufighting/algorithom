'''
231. Power of 2
326. Power of 3
342. power of 4
'''
class Solution(object):
    # 常规做法
    def isPowerOfTwo(self, n):
        if n < 1:
            return False
        base = 2
        while n > 1:
            if n % base != 0:
                return False
            n /= base
        return True

    #位运算
    def isPowerOfTwo(self, n):
        return n > 0 and n & n - 1 == 0
#==================================================================
    #常规做法
    def isPowerOfThree(self, n):
        if n < 1:
            return False
        base = 3
        while n > 1:
            if n % base != 0:
                return False
            n /= base

        return True
    #幂的性质：质数的高次幂余该质数的底次幂==0
    def isPowerOfThree(self, n):
        return n > 0 and 3**19 % n == 0
# ==================================================================

    # 4不是质数，不能用↑的方法。
    # 4的幂4的幂的二进制，只有一个1，并且在奇数位上，后面是偶数个0.因此与偶数位上都是1的数字想与结果为0
    # 4的幂一定是2的幂，n & n-1保证是2的幂，也就是保证只有一个1
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & num - 1 == 0 and num & int('101010101010101010101010101010', 2) == 0

s = Solution()
print(s.isPowerOfThree(3))
