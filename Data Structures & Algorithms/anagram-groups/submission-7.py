class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count_letters(s : str) -> Dict: 
            count = [0 for i in range(26)] # counter for letters
            for l in s: 
                count[ord(l) - ord('a')] += 1

            return count

        #store dict of anagrams, use 
        #dict.values() to get list after
        anagrams = {}

        #go through every string, and use the counter as key
        for s in strs: 
            key = tuple(count_letters(s))
            anagrams[key] = anagrams.get(key, []) + [s]

        return list(anagrams.values())
        
            
