def maxProfit(prices):
    l = 0
    r = 1

    maxP = float("-inf")

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
        else:
            l = r
        r += 1
    return maxP

# Driver Code

prices = [7,1,5,3,6,4]
print(maxProfit(prices))

