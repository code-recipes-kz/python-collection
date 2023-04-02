class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        unique_permutations = set()
        for perm in itertools.permutations(nums):
            if perm not in unique_permutations:
                unique_permutations.add(perm)
        return [list(perm) for perm in unique_permutations]