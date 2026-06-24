class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #idea: go through and look for target - nums[i], 
        #       keep a set to remember if we already saw it 
        
        seenBefore = {}

        for i in range(len(nums)):
            num = nums[i]
            lookingFor = target - num

            idx = seenBefore.get(lookingFor, -1)

            if idx != -1: 
                return [idx, i]

            else:
                seenBefore[num] = i



        