class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ""

        for i in range(2*len(s)-1):
            
            j = int(i/2) if i % 2 == 0 else int((i - 1)/2)
            k = int(i/2) if i % 2 == 0 else int((i + 1)/2)

            if len(max_str) < 1: 
                max_str = s[i]

            while j >= 0 and k < len(s) and s[j] == s[k]: 
                if len(max_str) < len(s[j:k+1]): 
                    max_str = s[j:k+1]

                j-=1 
                k+=1
            
        return max_str
            