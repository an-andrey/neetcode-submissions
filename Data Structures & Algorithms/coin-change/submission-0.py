class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0 
        
        for coin in coins: 
            for a in range(coin, amount+1):
                dp[a] = min(dp[a], 1+dp[a - coin])

        if dp[amount] == float('inf'): 
            return -1 
        else: 
            return dp[amount]