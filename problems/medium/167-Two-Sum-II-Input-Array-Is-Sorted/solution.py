class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num = {}
        for i, n in enumerate(numbers):
            if target - n in num:
                return [num[target - n] + 1,i + 1]
            num[n] = i