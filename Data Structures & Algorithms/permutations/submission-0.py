class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []

        def helper(start):

            # Base case
            if start == n:
                res.append(nums.copy())
                return

            for i in range(start, n):

                # Choose
                nums[start], nums[i] = nums[i], nums[start]

                # Explore
                helper(start + 1)

                # Backtrack / undo
                nums[start], nums[i] = nums[i], nums[start]

        helper(0)

        return res