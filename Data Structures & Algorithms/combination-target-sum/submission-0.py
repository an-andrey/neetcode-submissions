class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def helper(sum, i, numbers): 
            if sum == target: 
                combinations.append(numbers)
            elif sum < target: 
                for j in range(i, len(nums)):
                    helper(sum+nums[j], j, [*numbers, nums[j]])

        helper(0, 0, [])

        return combinations
