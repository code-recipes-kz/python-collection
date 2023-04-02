class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
    
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                p1, p2 = i+j, i+j+1
                s = product + result[p2]
                result[p2] = s % 10
                result[p1] += s // 10
        
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        
        return "".join(str(x) for x in result[start:])