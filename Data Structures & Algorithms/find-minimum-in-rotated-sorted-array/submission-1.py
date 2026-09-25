"""
3 scenarios: 

1. 12i(5)6
2. 56i(1)2
3. 56(i)


"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]

        if n == 2: 
            return min(nums[0], nums[1])

        r = n - 1
        l = 0 
        i = n//2

        while True:
            print(l, i, r)
            if nums[l] < nums[i] < nums[r]: 
                return nums[l]
            if nums[l] > nums[i] < nums[r]: 
                if nums[i-1] > nums[i] < nums[i+1]: 
                    return nums[i]
                else: 
                    if i-1 == l: 
                        return nums[l]
                    r = i 
                    i -= (i-l)//2
            if nums[l] < nums[i] > nums[r]: 
                if i+1 == r: 
                    return nums[r]
                l = i 
                i += (r-i)//2 

