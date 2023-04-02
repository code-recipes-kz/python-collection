class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def backtrack(combination, current_sum, index):
            if current_sum == target:
                result.append(combination)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if current_sum + candidates[i] > target:
                    break
                backtrack(combination + [candidates[i]], current_sum + candidates[i], i+1)
        
        backtrack([], 0, 0)
        return result