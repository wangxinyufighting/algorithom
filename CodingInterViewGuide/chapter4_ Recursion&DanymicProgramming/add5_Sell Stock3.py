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
