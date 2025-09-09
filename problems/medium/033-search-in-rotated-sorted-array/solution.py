class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if nums[0] == target:
            return 0
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[left] != target:
                left += 1
            elif nums[right] != target:
                right +=1
        else:
            return -1