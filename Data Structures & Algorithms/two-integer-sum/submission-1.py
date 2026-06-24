class Solution:
    def twoSum(self, nums : List[int], target:int):
        history = {}
            
        for i in range(len(nums)): 
            difference = target - nums[i]
            
            #if we haven't seen what we want,
            #add it to history and move on
            j = history.get(difference, -1)
            if j == -1:
                #store the index
                history[nums[i]] = i
            else: 
                return [j, i]
