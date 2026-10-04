class Solution:
    def countSubstrings(self, s: str) -> int:
        ttl = 0

        for c in range(1, 2*len(s)): 
            j = c // 2
            i = j
            if c % 2 == 0: 
                i -= 1
            
            while i >= 0 and j < len(s) and s[i] == s[j]: 
                ttl += 1
                i -= 1
                j += 1

        return ttl