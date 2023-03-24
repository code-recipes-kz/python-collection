class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        currEnd = 0
        maxIndex = 0
        
        for i in range(n-1):
            maxIndex = max(maxIndex, i + nums[i])
            
            if i == currEnd:
                jumps += 1
                currEnd = maxIndex
                
        return jumps