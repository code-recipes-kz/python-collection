class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev_value = 0
        total_sum = 0
        for symbol in s:
            value = roman_dict[symbol]
            if value > prev_value:
                total_sum += value - 2 * prev_value
            else:
                total_sum += value
            prev_value = value
        return total_sum