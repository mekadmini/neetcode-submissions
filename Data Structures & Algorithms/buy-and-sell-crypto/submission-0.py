class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            max_profit = max(max(max(prices[i+1:]) - prices[i], 0), max_profit)
        return max_profit