class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        if nums[0] != 0:
            return 0
        if nums[-1] == len(nums) - 1:
            return len(nums)
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left