'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def maxProfit(prices):
    # profit[len(prices)][交易次数][持有0 不持有1]
    if not prices:
        return 0

    profit = [[0] * 2 for _ in range(len(prices))]
    # 0不持有，1持有
    profit[0][0] = 0
    profit[0][1] = -prices[0]

    for i in range(1, len(prices)):
        profit[i][0] = max(profit[i - 1][0], profit[i - 1][1] + prices[i])
        profit[i][1] = max(profit[i - 1][1], profit[i - 1][0] - prices[i])

    return profit[-1][0]

#简化一下：
def maxProfit(prices):
    if not prices:
        return 0

    p_0 = 0
    p_1 = -prices[0]

    for i in range(1, len(prices)):
        p_0 = max(p_0, p_1+prices[i])
        p_1 = max(p_1, p_0-prices[i])

    return p_0


print(maxProfit([7,1,5,3,6,4]))