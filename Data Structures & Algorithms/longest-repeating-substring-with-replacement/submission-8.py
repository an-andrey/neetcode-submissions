import string

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0

        max_substr = ""
        max_len = 0

        char_counter = {c: 0 for c in string.ascii_uppercase}
        max_char = 'A'
        
        def get_max_char(): 
            max_char = 'A'
            max_freq = 0 

            for char, count in char_counter.items(): 
                if max_freq < count: 
                    max_char = char
                    max_freq = count

            return max_char

        while j < len(s): 
            char_counter[s[j]] += 1

            if char_counter[s[j]] > char_counter[max_char]: 
                max_char = s[j]

            # print(j-i+1, char_counter[max_char])
            if (j-i+1) - char_counter[max_char] <= k: # if still valid, increase
                if (j-i+1) > max_len: 
                    max_substr = s[i:j+1]
                    max_len = j - i + 1
                    # print(max_len)
                j += 1
            
            else: # if no longer valid 
                char_counter[s[i]] -= 1
                i += 1
                max_char = get_max_char()
                char_counter[s[j]] -= 1

        return max_len
                


