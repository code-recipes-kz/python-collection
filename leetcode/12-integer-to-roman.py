class Solution:
    def intToRoman(self, num: int) -> str:
        # Create a table of symbols and their values
        symbol_table = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        
        # Initialize an empty string to store the Roman numeral
        roman_numeral = ""
        
        # Iterate through the symbols in descending order
        for value, symbol in symbol_table.items():
            # Repeat while the remaining number is greater than or equal to the value
            while num >= value:
                # Subtract the value from the remaining number and add the symbol to the Roman numeral
                num -= value
                roman_numeral += symbol
        
        return roman_numeral