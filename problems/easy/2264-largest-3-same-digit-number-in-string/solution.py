class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_val = ""
        for n in range(1,len(num)- 1):
            if num[n-1] == num[n] == num[n+1]:
                max_val = max(max_val,num[n-1:n+2])
        return max_val             
