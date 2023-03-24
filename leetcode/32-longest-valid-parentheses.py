class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and stack[-1] != -1 and s[stack[-1]] == '(':
                    stack.pop()
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        return max_len