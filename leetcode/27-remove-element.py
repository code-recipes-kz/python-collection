class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # pointer to iterate through array
        j = 0  # pointer to keep track of next position to place an element

        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1

        return j