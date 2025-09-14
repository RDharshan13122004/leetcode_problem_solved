import heapq
from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent  = Counter(nums)
        return [num for num,_ in heapq.nlargest(k,frequent.items(),key=lambda x:x[1])]