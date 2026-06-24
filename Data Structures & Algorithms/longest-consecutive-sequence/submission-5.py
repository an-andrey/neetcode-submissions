class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_unique = set(nums)

        max_len = 0

        for n in nums: 
            if n+1 in nums: # only check max of a sequence
                continue
            else:
                longest_sequence = 1 
                if max_len < longest_sequence: 
                    max_len = longest_sequence

                sequence = True
                i = 1

                while sequence == True: 
                    if n-i in nums:
                        longest_sequence += 1
                        i += 1
                    else:
                        sequence = False
                        if max_len < longest_sequence: 
                            max_len = longest_sequence

        return max_len
        

