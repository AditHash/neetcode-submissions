class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            req = target - num

            if req in seen:
                return [seen[req], i]

            seen[num] = i