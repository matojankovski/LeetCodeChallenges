def maxProfit(prices):
    max_profit = 0
    left, right = 0, 1
    while right < len(prices):
        diff = prices[right] - prices[left]
        if prices[left] < prices[right]:
            max_profit = max(max_profit, diff)
        else:
            left = right
        right +=1
    return max_profit
`







prices = [7,1,5,3,6,4]
print(maxProfit(prices))