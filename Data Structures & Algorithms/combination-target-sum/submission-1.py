class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        temp = []

        nums.sort()

        def helper(nums, res, temp, remain, start):

            # Target reached
            if remain == 0:
                res.append(temp.copy())
                return

            # Target exceeded
            if remain < 0:
                return

            for i in range(start, len(nums)):

                # Choose
                temp.append(nums[i])

                # Explore
                # i, NOT i + 1
                helper(nums, res, temp, remain - nums[i], i)

                # Backtrack
                temp.pop()

        helper(nums, res, temp, target, 0)

        return res