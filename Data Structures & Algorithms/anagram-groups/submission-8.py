class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s, t): 
            if len(s) != len(t): 
                return False

            counterS = {}
            counterT = {}

            for i in range(len(s)): 
                counterS[s[i]] = counterS.get(s[i], 0) + 1
                counterT[t[i]] = counterT.get(t[i], 0) + 1

            return counterS == counterT

        anagrams = [[strs[0]]]

        for s_idx in range(1, len(strs)): # skipping the first one
            s = strs[s_idx]
            t = ""
            grp_idx = None
            for anagram_grp_idx, anagram_grp in enumerate(anagrams): 
                t = anagram_grp[0]

                if isAnagram(s,t):
                    grp_idx = anagram_grp_idx
                    break

            if grp_idx is None: 
                anagrams.append([s])
            else: 
                anagrams[grp_idx].append(s)
                
        return anagrams 




