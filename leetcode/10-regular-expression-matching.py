class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize the dp array
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: both strings are empty
        dp[0][0] = True
        
        # Handle patterns with *
        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # Fill the dp array
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        
        # Return the result
        return dp[-1][-1]