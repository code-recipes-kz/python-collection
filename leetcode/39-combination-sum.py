class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, target, curr_list):
            if target == 0:
                res.append(curr_list[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                curr_list.append(candidates[i])
                backtrack(i, target - candidates[i], curr_list)
                curr_list.pop()

        backtrack(0, target, [])
        return res