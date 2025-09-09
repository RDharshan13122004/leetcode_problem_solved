class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        for row in matrix:
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = (left + right)//2
                if row[mid] == target:
                    res = True
                    return res
                elif row[mid] < target:
                    left = mid + 1
                elif row[mid] > target:
                    right = mid - 1
        if res:
            return True
        else: 
            return False