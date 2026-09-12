class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)        
        # ans array
        ans = []
        temp = []

        def helper(nums, start, ans, temp):
            ans.append(temp.copy())

            for i in range(start, n):
                temp.append(nums[i])
                helper(nums, i+1, ans, temp)
                temp.pop() # or temp.remove(n-1)
        helper(nums, 0, ans, temp)
        return ans
            

