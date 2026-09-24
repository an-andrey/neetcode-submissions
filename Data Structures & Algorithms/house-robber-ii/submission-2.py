class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = [0] * (len(nums) - 1)
        dp2 = [0] * (len(nums))

        if len(nums) == 1: 
            return nums[0]
        if len(nums) == 2: 
            return max(nums[0], nums[1])
        if len(nums) == 3: 
            return max(nums[0], max(nums[1], nums[2]))
        
        dp1[0] = nums[0]
        dp1[2] = nums[0] + nums[2]
        
        dp2[1] = nums[1]
        dp2[2] = nums[2]
        
        for i in range(3, len(nums)): 
            if i < len(nums)-1:
                dp1[i] = max(dp1[i-2], dp1[i-3]) + nums[i]
            dp2[i] = max(dp2[i-2], dp2[i-3]) + nums[i]

        return max(max(dp1[-1], dp1[-2]), max(dp2[-2], dp2[-1]))