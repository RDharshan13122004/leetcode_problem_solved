class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1,len(heights)):
            curr = heights[i]
            curr_name = names[i]
            j = i - 1
            while j >= 0 and curr > heights[j]:
                heights[j+1] = heights[j]
                names[j+1] = names[j]
                j-=1
            heights[j+1] = curr
            names[j+1] = curr_name
        return names
        