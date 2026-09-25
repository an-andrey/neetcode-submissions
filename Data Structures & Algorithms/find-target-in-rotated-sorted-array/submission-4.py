class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(nums, target): 
            l, r = 0, len(nums)-1

            while l <= r: 
                m = (l + r)//2

                if nums[m] == target: 
                    return m
                elif nums[m] > target: 
                    r = m-1
                else: 
                    l = m+1

            return -1

        l = 0 
        r = len(nums) - 1

        while l < r: 
            mid = l + (r-l)//2
            if nums[mid] < nums[r]: 
                r = mid
            else: 
                l = mid + 1

        min_idx = l

        result_left = binary_search(nums[:l], target)
        result_right = binary_search(nums[l:], target)

        if result_right == -1: 
            return result_left

        else: 
            return result_right+l

            

            