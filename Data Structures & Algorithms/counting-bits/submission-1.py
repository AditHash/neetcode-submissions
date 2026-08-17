class Solution:
    def countBits(self, n: int) -> List[int]:
        
        arr = []
        ans = []
        i = 0
        while (i <= n):
            arr.append(i)
            i += 1
        # return arr

        for num in arr:
            count = 0
            while (num != 0):
                num = num & (num-1)
                count += 1
            ans.append(count) 
        return ans

        