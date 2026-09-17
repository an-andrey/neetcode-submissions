class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w = 0
        i = 0 

        while i < len(abbr) and w < len(word): 
            if abbr[i] == word[w]: 
                w += 1
                i += 1
                pass

            else: 
                if abbr[i].isnumeric(): 
                    if abbr[i] == "0": 
                        return False

                    j = i
                    while j < len(abbr) and abbr[j].isdigit(): 
                        j += 1
                    
                    len_abbr_n = int(abbr[i:j])
                    i = j
                    w += len_abbr_n
                     
                else: 
                    return False

        return i == len(abbr) and w == len(word)
 

