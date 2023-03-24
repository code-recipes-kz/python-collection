class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                # Add the current permutation to the result list
                res.append(nums[:])
            for i in range(start, len(nums)):
                # Swap the current element with the element at index i
                nums[start], nums[i] = nums[i], nums[start]
                # Recursively generate all the permutations starting from start+1
                backtrack(start + 1)
                # Swap back the elements to restore the original array
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0)
        return res