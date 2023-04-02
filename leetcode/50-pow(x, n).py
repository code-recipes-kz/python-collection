class Solution:
    def myPow(self, x: float, n: int) -> float:
       # Check for negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        while n > 0:
            # If the exponent is odd, multiply the result by x
            if n % 2 == 1:
                result *= x
            
            # Square x and divide the exponent by 2
            x *= x
            n //= 2
        
        return result