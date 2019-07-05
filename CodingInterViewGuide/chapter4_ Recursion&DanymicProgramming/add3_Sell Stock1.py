def maxProfit(prices):
    if not prices:
        return 0
    f = [0] * len(prices)
    lowestprice = float('inf')
    for i in range(len(prices)):
        lowestprice = min(lowestprice, prices[i])
        f[i] = max(prices[i] - lowestprice, f[i-1])

    print(f)
    return f[-1]


print(maxProfit([7,1,5,3,7,4]))
