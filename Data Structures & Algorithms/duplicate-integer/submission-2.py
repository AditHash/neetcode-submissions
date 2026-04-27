class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
        # freq = {} 
        # flag = False
        
        # for i in nums:
        #     if i in freq:
        #         freq[i] += 1
        #         flag = True
        #         break
        #     else:
        #         freq[i] = 1
        # return flag


        