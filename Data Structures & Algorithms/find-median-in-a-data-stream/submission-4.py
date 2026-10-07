class MedianFinder:
    def __init__(self):
        self.lower = []
        self.upper = []
        self.order = 1

    def addNum(self, num: int) -> None:
        if self.order == 1: # lower half case
            if self.upper == [] or num < self.upper[0]:
                heapq.heappush(self.lower, -1*num)
            else: 
                tmp = heapq.heappop(self.upper)
                heapq.heappush(self.upper, num)
                heapq.heappush(self.lower, -1*tmp)
        else: 
            if self.lower == [] or num > -1*self.lower[0]:
                heapq.heappush(self.upper, num)
            else: 
                tmp = -1*heapq.heappop(self.lower)
                heapq.heappush(self.lower, -1*num)
                heapq.heappush(self.upper, tmp)

        self.order *= -1

    def findMedian(self) -> float:
        if len(self.lower) == len(self.upper): 
            return (-1*self.lower[0] + self.upper[0])/2

        if self.lower[0] == 0:
            return self.lower[0]
            
        return -1.0*self.lower[0]
        
        