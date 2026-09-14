class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []
        temp = []

        def helper(candidates, res, temp, remain, start):

            # Target reached
            if remain == 0:
                res.append(temp.copy())
                return

            # Try all candidates
            for i in range(start, len(candidates)):

                # Skip duplicate choices at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since sorted, no later number can work
                if candidates[i] > remain:
                    break

                # Choose
                temp.append(candidates[i])

                # Explore
                # i + 1 because each element can be used only once
                helper(candidates, res, temp, remain - candidates[i], i + 1)

                # Backtrack
                temp.pop()

        helper(candidates, res, temp, target, 0)

        return res