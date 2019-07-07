'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def maxProfit(prices):
    if not prices:
        return 0

    p = [[[0] * 2] * 3 for _ in range(len(prices))]
    # 1持有， 0不持有
    p[0][0][0] = p[0][1][0] = p[0][2][0] = 0
    p[0][0][1] = p[0][1][1] = p[0][2][1] = float('-inf')

    for i in range(1, len(prices)):
        for k in range(2, 0, -1):
            p[i][k][0] = max(p[i - 1][k][0], p[i - 1][k][1] + prices[i])
            p[i][k][1] = max(p[i - 1][k][1], p[i - 1][k-1][0] - prices[i])

    print(p)

    return p[-1][-1][0]

maxProfit([3,3,5,0,0,3,1,4])
