class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = 0
        for i in arr:
            if i % 2 == 1 or i == 1:
                odd += 1
            else:
                odd = 0
            if odd == 3:
                return True
        else:
            return False
        