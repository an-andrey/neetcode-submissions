class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_unique = set(nums)

        max_len = 0

        for n in nums_unique: 
            if n+1 in nums_unique: # only check max of a sequence
                continue

            current_sequence = 1 

            while n - current_sequence in nums_unique: 
                current_sequence += 1
            
            if max_len < current_sequence: 
                max_len = current_sequence

        return max_len
    

