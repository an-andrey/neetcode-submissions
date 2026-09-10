class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i-1] <= min_so_far:
                min_so_far = prices[i-1]
        
            trade_profit = prices[i] - min_so_far
            if trade_profit > profit: 
                profit = trade_profit

        return profit

