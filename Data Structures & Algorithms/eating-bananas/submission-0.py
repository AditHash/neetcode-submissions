class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # print(spiles)
        max_k = max(piles)
        min_k = 1

        while min_k < max_k:
            mid = (min_k + max_k) // 2

            total_hours = 0

            for pile in piles:
                total_hours += (pile + mid - 1) // mid

            if total_hours <= h:
                max_k = mid
            else:
                min_k = mid + 1

        return min_k

        