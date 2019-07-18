'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
这个题看起来很简单，但其实有个“溢出”这一问题，需要注意。

'''

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        t = abs(x)
        while t != 0:
            result = result * 10 + t % 10
            t //= 10
        if result < -2 ** 31 or result > 2 ** 31:
            return 0
        return result if x > 0 else -result


s = Solution()
print(s.reverse(-120))