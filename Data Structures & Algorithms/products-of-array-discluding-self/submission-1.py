class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev_prods = [1 for i in nums]
        post_prods = [1 for i in nums]
        
        for i in range(1, len(nums)):
            prev_prods[i] = (prev_prods[i-1] * nums[i-1])
        
        for i in range(len(nums)-2, -1, -1):
            post_prods[i] = (post_prods[i+1] * nums[i+1])
        
        return [prev_prods[i] * post_prods[i] for i in range(len(nums))]

