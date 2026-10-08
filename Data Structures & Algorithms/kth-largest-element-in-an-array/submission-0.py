class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []

        for n in nums: 
            if len(arr) == k: 
                heapq.heappushpop(arr, n)
            else: 
                heapq.heappush(arr, n)

        return arr[0]