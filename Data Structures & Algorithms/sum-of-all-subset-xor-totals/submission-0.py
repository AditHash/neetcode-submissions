class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        res = []
        currsum = 0
        def helper(index, currsum, res, nums):
            # base case
            if (index == n):
                res.append(currsum)
                return
            # include the number
            helper(index + 1, currsum ^ nums[index], res, nums)
            # exclude the number
            helper(index + 1, currsum, res, nums)

        helper(0, 0, res, nums)
        ans = sum(res)
        return ans