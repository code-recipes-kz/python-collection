class Solution:
    def myAtoi(self, s: str) -> int:
         # Read in and ignore any leading whitespace
        i = 0
        while i < len(s) and s[i].isspace():
            i += 1
        
        # Check if the next character is '-' or '+'
        sign = 1
        if i < len(s) and s[i] in ('-', '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Read in the digits until the next non-digit character or the end of the input is reached
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        # Change the sign as necessary
        num *= sign
        
        # Clamp the integer to the range [-2^31, 2^31 - 1]
        max_int = (1 << 31) - 1
        min_int = -(1 << 31)
        if num > max_int:
            return max_int
        elif num < min_int:
            return min_int
        else:
            return num