class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums) - 1
        for i in range(len(nums)):
            mid = (min + max)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                max = mid - 1
            elif target > nums[mid]:
                min = mid + 1        
        else:
            return -1
            
        