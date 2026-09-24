class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def helper(ttl, i, numbers): 
            if ttl == target: 
                combinations.append(numbers.copy())
            elif ttl < target: 
                for j in range(i, len(nums)):
                    numbers.append(nums[j])
                    helper(ttl+nums[j], j, numbers)
                    numbers.pop()

        helper(0, 0, [])

        return combinations
