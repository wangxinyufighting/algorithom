'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def restoreIpAddresses(self, s: str):
        if not s or len(s) < 4 or len(s) > 12:
            return []
        n = len(s)
        result = []

        def backtrack(pos, temp, dots=3):
            if dots == 0:
                result.append(temp)
                return

            for i in range(pos, pos+3):
                if int(s[pos:i+1]) < 255 and s[pos:i+1][0] != '0':
                    backtrack(i+1, temp + '.' + s[pos:i+1], dots - 1)
                else:
                    continue

        backtrack(0, '')
        return result

s = Solution()
print(s.restoreIpAddresses('25525511135'))

