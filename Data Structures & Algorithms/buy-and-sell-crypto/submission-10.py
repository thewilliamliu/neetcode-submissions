class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy, sell = 0, 1
        
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell # Get to the lower buying point, don't just increment.
    
            profit = max(profit, prices[sell] - prices[buy])

            sell += 1

        return profit
           