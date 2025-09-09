class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        N = abs(n)
        result = 1
        
        while N > 0:
            if N % 2 == 1:  
                result *= x
            x *= x
            N //= 2
        
        return result if n > 0 else 1 / result