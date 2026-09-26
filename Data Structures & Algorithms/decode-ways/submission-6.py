class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        strs = [f"{i}" for i in range(1,27)] # constant time lookup still

        if len(s) == 1: 
            if (1 <= int(s[0]) <= 26): 
                return 1
            else: 
                return 0
            
        if s[0] in strs:
            dp[0] = 1 
        else:
            return 0

        for i in range(1, len(s)): 
            if s[i] in strs: 
                dp[i] += dp[i-1]

            if s[i-1:i+1] in strs: 
                dp[i] += 1 if i == 1 else dp[i-2]
            
            if dp[i] == 0: 
                return 0

        return dp[-1]


