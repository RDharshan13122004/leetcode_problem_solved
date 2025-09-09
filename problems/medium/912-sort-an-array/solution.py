class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.Msort(nums)
        return nums

    def Msort(self,arr):   
        if len(arr) > 1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]

            self.Msort(left)
            self.Msort(right)

            lp = rp = fp = 0

            while lp < len(left) and rp < len(right):
                if left[lp] < right[rp]:
                    arr[fp] = left[lp]
                    lp += 1
                else:
                    arr[fp] = right[rp]
                    rp += 1
                fp += 1

            while lp < len(left):
                arr[fp] = left[lp]
                lp += 1
                fp += 1

            while rp < len(right):
                arr[fp] = right[rp]
                rp += 1
                fp += 1