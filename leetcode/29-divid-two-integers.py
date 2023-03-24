class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Convert dividend and divisor to absolute values
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Initialize quotient and remainder
        quotient = 0
        remainder = dividend

        # Subtract divisor from remainder until remainder < divisor
        while remainder >= divisor:
            shift = 0
            while (divisor << shift) <= remainder:
                shift += 1
            shift -= 1
            quotient += 1 << shift
            remainder -= divisor << shift

        # Apply sign to quotient
        quotient *= sign

        # Check for integer overflow
        if quotient > (2**31 - 1):
            return 2**31 - 1
        elif quotient < (-2**31):
            return -2**31
        else:
            return quotient