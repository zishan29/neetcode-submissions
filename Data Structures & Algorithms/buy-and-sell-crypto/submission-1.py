class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit > 0:
                maxProfit = max(profit, maxProfit)
                sell += 1
            else:
                buy = sell
            sell += 1
        
        return maxProfit