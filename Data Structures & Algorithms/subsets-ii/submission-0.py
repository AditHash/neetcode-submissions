class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # first sort the nums
        nums.sort()

        res = []
        temp = []

        def helper(res, temp, nums, index):
            # base case
            res.append(temp.copy())

            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                temp.append(nums[i])
                helper(res, temp, nums, i + 1)
                temp.pop()
        # call the function
        helper(res, temp, nums, 0)
        return res


        