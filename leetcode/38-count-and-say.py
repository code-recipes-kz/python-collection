class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n-1)
        result = ""
        i = 0
        while i < len(prev):
            count = 1
            while i < len(prev)-1 and prev[i] == prev[i+1]:
                count += 1
                i += 1
            result += str(count) + prev[i]
            i += 1
        return result