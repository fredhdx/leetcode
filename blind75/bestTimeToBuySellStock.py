class Solution:
    def maxProfit(self, prices):
        lower = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < lower:
                lower = price
            else:
                max_profit = max(max_profit, price - lower)
        return max_profit
                