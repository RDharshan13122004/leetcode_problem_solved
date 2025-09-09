class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) > 1:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]

            self.sortColors(left)
            self.sortColors(right)

            lp = rp = fp = 0

            while lp < len(left) and rp < len(right):
                if left[lp] < right[rp]:
                    nums[fp] = left[lp]
                    lp +=1

                else:
                    nums[fp] = right[rp]
                    rp +=1
                fp +=1

            while lp < len(left):
                nums[fp] = left[lp]
                lp += 1
                fp += 1

            while rp < len(right):
                nums[fp] = right[rp]
                rp += 1
                fp += 1
        