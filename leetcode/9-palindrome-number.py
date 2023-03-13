class Solution:
    def isPalindrome(self, x: int) -> bool:
         # Convert the integer to a string
        s = str(x)
        
        # Check if the string is the same when read forwards and backwards
        return s == s[::-1]