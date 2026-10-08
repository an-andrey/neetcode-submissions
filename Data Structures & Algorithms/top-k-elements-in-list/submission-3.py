class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]

        for n, freq in counter.items(): 
            buckets[freq].append(n)

        output = []

        for i in range(len(nums), -1, -1): 
            for n in buckets[i]:
                output.append(n)
                if len(output) == k: 
                    return output

        return output