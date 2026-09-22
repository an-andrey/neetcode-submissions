class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        combinations = []
        
        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i-1]:
                continue 

            l = i + 1
            r = len(nums) - 1

            while l < r: 
                sum = nums[l] + nums[r]

                if nums[i] == -1*sum:
                    combinations.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    while l < r and nums[l] == nums[l+1]: 
                        l += 1

                    r -= 1
                    l += 1

                elif nums[i] < -1*sum: 
                    l += 1

                else: 
                    r -= 1

        return combinations