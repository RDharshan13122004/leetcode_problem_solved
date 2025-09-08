class MedianFinder:

    def __init__(self):
        self.stack = []

    def addNum(self, num: int) -> None:
        self.stack.append(num)

    def findMedian(self) -> float:
        self.stack.sort()
        n = len(self.stack) 
        if n % 2 == 0:
            mid1, mid2 = self.stack[n // 2 - 1], self.stack[n // 2]
            return (mid1 + mid2) / 2.0
        else:
            return float(self.stack[n // 2])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()