class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums: 
            counts[n] = 1 + counts.get(n, 0)

        for n, count in counts.items(): 
            freq[count].append(n)

        output = []

        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]: 
                output.append(num)
                if len(output) == k: 
                    return output