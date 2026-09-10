class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        max_substring_len = 0
        seen_letters = set()

        for i in range(len(s)):
            if s[i] in seen_letters: 
                while substring[0] != s[i]: 
                    seen_letters.remove(substring[0])
                    substring = substring[1:]

                substring = substring[1:]
                substring += s[i]
            
            else: 
                seen_letters.add(s[i])
                substring += s[i]
            
            max_substring_len = max(len(substring), max_substring_len)

        return max_substring_len

    """
    abcdc

    """