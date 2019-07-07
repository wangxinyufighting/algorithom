'''
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def maxProfit(self, prices, fee):
        if not prices:
            return 0

        f_0 = 0
        f_1 = -prices[0] - fee

        for i in range(1, len(prices)):
            temp = f_0
            f_0 = max(f_0, f_1 + prices[i])
            f_1 = max(f_1, f_0 - prices[i] - fee)

        return f_0

    #         f = [[0]*2 for _ in range(len(prices))]
    #         f[0][0] = 0
    #         f[0][1] = -prices[0] - fee

    #         for i in range(1,len(prices)):
    #             f[i][0] = max(f[i-1][0], f[i-1][1] + prices[i])
    #             f[i][1] = max(f[i-1][1], f[i-1][0] - prices[i] - fee)

    #         return f[-1][0]

s = Solution()
s.maxProfit([1, 3, 2, 8, 4,  9], 2)
