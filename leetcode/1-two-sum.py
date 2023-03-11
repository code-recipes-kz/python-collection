class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(numbers)):
            num = numbers[i]
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
