class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, parens=[]):
            if left:         # If there are any left parenthesis remaining
                generate(p + '(', left-1, right)   # Add a left parenthesis
            if right > left: # If there are more right than left parenthesis
                generate(p + ')', left, right-1)   # Add a right parenthesis
            if not right:    # If there are no more right parenthesis remaining
                parens.append(p)  # Append the generated combination to the result
            return parens

        return generate('', n, n) # Call the helper function with initial values