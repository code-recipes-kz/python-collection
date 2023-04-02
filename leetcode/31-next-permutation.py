class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1: find the first element that is smaller than its next element
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # Step 2: find the first element greater than nums[i] from right
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: reverse the subarray nums[i+1:]
        left, right = i+1, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1