class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_subarray = sum(nums[:k])
        max_val = window_subarray
        for i in range(k,len(nums)):
            window_subarray += nums[i] - nums[i - k]
            max_val = max(max_val,window_subarray)
        return max_val / k