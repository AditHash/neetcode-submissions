class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        n = len(piles)
        low = 1
        high = max(piles)
        ans = 0

        def helper(sp, piles, n, h):
            hour = 0

            for i in range(n):
                hour = hour + math.ceil(piles[i] / sp)

            if hour <= h:
                return True

            return False

        while (low <= high):
            mid = (low + high) // 2

            if helper(mid, piles, n, h) == True:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans