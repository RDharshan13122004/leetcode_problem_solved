class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(1,len(nums)):
            curr = nums[i]
            j = i-1
            while j>=0 and curr < nums[j]:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = curr
            if nums[j] == curr:
                return True 
        else:
            return False