class Solution:
    def maxArea(self, heights: List[int]) -> int:
        width = 0 

        start = 0
        end = len(heights) - 1

        max_vol = 0 

        while start != end: 
            curr_vol = (end - start) * min(heights[start], heights[end])

            max_vol = max(max_vol, curr_vol)

            if heights[start] > heights[end]: 
                end -= 1

            else: 
                start += 1
        return max_vol