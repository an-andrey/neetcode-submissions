class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numbers = {}

        for i, n in enumerate(nums):
            looking_for = target - n

            if looking_for in numbers:
                return [numbers[looking_for], i]

            else:
                numbers[n] = i
        return    