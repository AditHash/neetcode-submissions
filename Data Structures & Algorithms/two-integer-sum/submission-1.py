class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            req = target - num
            if req in seen:
                return [seen[req], i]
            seen[num] = i
            
            
        
        
        
        
        
        # l = len(nums)

        # for i in range(l):
        #     num = nums[i]
        #     req = target - num
        #     for j in range(i+1, l):
        #         if nums[j] == req:
        #             return[i,j]
        #             break

        