class Solution:
    def reverse(self, x: int) -> int:
        # Check if x is negative
        negative = x < 0
        if negative:
            x = -x
    
        # Reverse the digits of x and check the range
        reversed_x = 0
        max_int = (1 << 31) - 1
        min_int = -(1 << 31)
        while x > 0:
            digit = x % 10
            if reversed_x > max_int // 10 or (reversed_x == max_int // 10 and digit > max_int % 10):
                return 0
            if reversed_x < min_int // 10 or (reversed_x == min_int // 10 and digit < min_int % 10):
                return 0
            reversed_x = reversed_x * 10 + digit
            x //= 10
        
        # Return the reversed integer with the original sign
        if negative:
            return -reversed_x
        else:
            return reversed_x