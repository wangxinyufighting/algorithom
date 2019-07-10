'''
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
'''
def maxProfit(prices):
    if len(prices) < 2:
        return 0

    f = [[0] * 2 for _ in range(len(prices))]
    # 0 不持有
    f[0][0] = 0
    # 1 持有
    f[0][1] = -prices[0]
    f[1][0] = 0

    #由于冷冻期的出现，使得i>1时处理不一样，要注意。
    for i in range(1, len(prices)):
        if i > 1:
            f[i][0] = max(f[i - 1][0], f[i - 1][1] + prices[i])
            f[i][1] = max(f[i - 1][1], f[i - 2][0] - prices[i])
        else:
            '''
            f[1]持有股票时，有两个情况。
            1.f[0]持有，f[1]没变
            2.f[0]未持有，f[1]买入。此时没有冷冻期，因为i=1。所以和上面处理不一样。
            '''
            f[i][0] = max(f[i - 1][0], f[i - 1][1] + prices[i])
            f[i][1] = max(f[i - 1][1], f[i - 1][0] - prices[i])

    return f[-1][0]