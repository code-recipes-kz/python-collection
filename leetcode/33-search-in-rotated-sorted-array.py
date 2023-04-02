class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        # find the pivot index
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # perform binary search in the appropriate half
        left, right = 0, n-1
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1