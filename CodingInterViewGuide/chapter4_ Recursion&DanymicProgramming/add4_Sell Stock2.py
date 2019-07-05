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