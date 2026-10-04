class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [0] * (2*len(s))
        dp[0] = 0

        for c in range(1, len(dp)): 
            j = c // 2
            i = j
            if c % 2 == 0: 
                i -= 1
            
            while i >= 0 and j < len(s) and s[i] == s[j]: 
                dp[c] += 1
                i -= 1
                j += 1
            
            dp[c] += dp[c-1]

        return dp[-1]