class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)

        for i in range(l):
            num = nums[i]
            req = target - num
            for j in range(i+1, l):
                if nums[j] == req:
                    return[i,j]
                    break

        