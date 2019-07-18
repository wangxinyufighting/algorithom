'''
请你来实现一个 atoi 函数，使其能将字符串转换成整数。
说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。
如果数值超过这个范围，qing返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

示例 1:

输入: "42"
输出: 42
示例 2:

输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
     因此返回 INT_MIN (−231) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-to-integer-atoi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


'''
这个题一定要注意细节
'''
class Solution:
    def myAtoi(self, str_: str) -> int:
        if not str_:
            return 0
        flag = True
        index = 0
        result = 0

        while index < len(str_) and str_[index] == ' ':
            index += 1
        #判断一下 str_是否只是“ ”*n，若是，下面就不要执行了，否则会越界
        if index == len(str_):
            return 0

        if str_[index] == '+':
            index += 1
        elif str_[index] == '-':
            flag = False
            index += 1

        nums = [str(t) for t in range(10)]
        for i in range(index, len(str_)):
            if str_[i] not in nums:
                break
            result = result * 10 + int(str_[i])

            if flag and result >= 2 ** 31:
                return 2**31 - 1
            if not flag and -result < -2**31:
                return -2**31

        return result if flag else -result

s = Solution()
print(-2**31)
print(s.myAtoi('+10'))