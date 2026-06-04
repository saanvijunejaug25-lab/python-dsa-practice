def maxProfit(prices):
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
            else:
                left = right
            right += 1
        return max_profit
prices = [7,1,5,3,6,4]

s1 = maxProfit(prices)
print(s1)
        