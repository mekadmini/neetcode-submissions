class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            max_profit = max(max(prices[i+1:]) - prices[i], max_profit)
        return max_profit