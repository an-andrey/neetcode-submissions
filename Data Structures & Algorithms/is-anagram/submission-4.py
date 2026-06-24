class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counterS = {}
        counterT = {}

        #here, both are the same size
        for i in range(len(s)): 
            counterS[s[i]] = counterS.get(s[i], 0) + 1
            counterT[t[i]] = counterT.get(t[i], 0) + 1

        #now that we have the count, check in O(n) time that they're 
        #equal
        return counterS == counterT
        