class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {} 
        flag = False
        
        for i in nums:
            if i in freq:
                freq[i] += 1
                flag = True
                break
            else:
                freq[i] = 1
        return flag


        