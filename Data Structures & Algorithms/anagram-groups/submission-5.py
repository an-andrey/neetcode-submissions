class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for word in strs:
            sorted_word = str(sorted(word))

            if sorted_word in anagrams: 
                anagrams[sorted_word].append(word)
            
            else: 
                anagrams[sorted_word] = [word]
            
        return list(anagrams.values())