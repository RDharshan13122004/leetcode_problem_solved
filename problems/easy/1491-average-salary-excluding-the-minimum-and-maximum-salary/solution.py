class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(0)
        salary.pop()

        avg = sum(salary)/len(salary)
        return avg