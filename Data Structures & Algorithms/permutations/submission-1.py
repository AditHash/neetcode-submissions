class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []

        def helper(nums, res, start):

            # Base case
            if start == len(nums):
                res.append(nums.copy())
                return

            # Try every element from start to n
            for i in range(start, len(nums)):

                # Choose
                nums[start], nums[i] = nums[i], nums[start]

                # Explore
                helper(nums, res, start + 1)

                # Backtrack / undo
                nums[start], nums[i] = nums[i], nums[start]

        helper(nums, res, 0)

        return res