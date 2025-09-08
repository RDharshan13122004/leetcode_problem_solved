class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        self.merge(nums1)
        n = len(nums1)

        if n % 2 == 0:
            mid1 = nums1[n//2 - 1]
            mid2 = nums1[n//2]
            median = (mid1 + mid2)/2
        else:
            median = nums1[n//2]
        return median

    def merge(self,arr):
        if len(arr) > 1:

            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]

            self.merge(left)
            self.merge(right)

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